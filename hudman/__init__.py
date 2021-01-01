# coding=utf-8

# This file is a part of HUD mirror script. For more information
# visit official site: https://www.easycoding.org/projects/hudman
#
# Copyright (c) 2016 - 2019 EasyCoding Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import calendar
import datetime
import email.utils
import hashlib
import json
import logging
import os
import sys
import time
import urllib.request
import xml.dom.minidom

from .hudlist import HUDEntry
from .hudmsg import HUDMessages, HUDSettings


class HUDMirror:
    @staticmethod
    def gmt2unix(gtime: str) -> int:
        """
        Convert datetime string to unixtime.
        :param gtime: Datetime string.
        :return: UnixTime integer.
        :rtype: int
        """
        do = datetime.datetime.strptime(gtime, '%Y-%m-%dT%H:%M:%SZ')
        return int(calendar.timegm(do.timetuple()))

    @staticmethod
    def hth2unix(gtime: str) -> int:
        """
        Convert datetime string in HTTP-header format to unixtime.
        :param gtime: Datetime string in HTTP-header format.
        :return: UnixTime integer.
        :rtype: int
        """
        return int(calendar.timegm(email.utils.parsedate(gtime)))

    @staticmethod
    def callgithubapi(repourl: str) -> list:
        """
        Call GitHub API and fetch useful information about project.
        :param repourl: GitHub repository URL.
        :return: List with SHA1 hash and datetime of latest commit.
        :rtype: list
        """
        url = repourl.replace('https://github.com/', 'https://api.github.com/repos/') + '/commits?per_page=1'
        response = urllib.request.urlopen(
            urllib.request.Request(url, data=None, headers={'User-Agent': HUDSettings.ua_curl}))
        if response.status != 200:
            raise Exception(HUDMessages.gh_errcode.format(response.status))
        data = json.loads(response.read().decode('utf-8'))
        return [data[0]['sha'], HUDMirror.gmt2unix(data[0]['commit']['committer']['date'])]

    @staticmethod
    def getlhmurl(url: str) -> str:
        """
        Call HTTP HEAD method to retrieve last modification time
        of specified URL.
        :param url: URL of remote file.
        :return: Last modification time.
        :rtype: str
        """
        request = urllib.request.Request(url, data=None, headers={'User-Agent': HUDSettings.ua_curl}, method='HEAD')
        response = urllib.request.urlopen(request)
        if response.status != 200:
            raise Exception(HUDMessages.oth_errcode.format(response.status))
        headers = response.info()
        return headers['Last-Modified']

    @staticmethod
    def downloadfile(url: str, name: str, outdir: str) -> str:
        """
        Download file from Internet and save it to specified directory.
        :param url: URL of remote file.
        :param name: Name of result file.
        :param outdir: Output directory.
        :return: Full local path of downloaded file.
        :rtype: str
        """
        fdir = os.path.join(outdir, name)
        if not os.path.exists(fdir):
            os.makedirs(fdir)
        filepath = os.path.join(fdir, '{}.zip'.format(name))
        request = urllib.request.Request(url, data=None, headers={'User-Agent': HUDSettings.ua_wget})
        with urllib.request.urlopen(request) as response, open(filepath, 'wb') as result:
            result.write(response.read())
        return filepath

    @staticmethod
    def renamefile(fname: str, chash: str) -> str:
        """
        Rename file using it's hash.
        :param fname: Source file name.
        :param chash: Source file hash sum.
        :return: Full local path of renamed file.
        :rtype: str
        """
        fdir = os.path.dirname(fname)
        result = os.path.join(fdir, '{}_{}.zip'.format(os.path.splitext(os.path.basename(fname))[0], chash[:8]))
        if os.path.isfile(result):
            os.remove(result)
        os.rename(fname, result)
        return result

    @staticmethod
    def sha1hash(fname: str) -> str:
        """
        Calculate SHA1 hash sum of specified file.
        :param fname: Source file name.
        :return: SHA1 hash of source file.
        :rtype: str
        """
        return hashlib.sha1(open(fname, 'rb').read()).hexdigest()

    @staticmethod
    def sha512hash(fname: str) -> str:
        """
        Calculate SHA-512 hash sum of specified file.
        :param fname: Source file name.
        :return: SHA-512 hash of source file.
        :rtype: str
        """
        return hashlib.sha512(open(fname, 'rb').read()).hexdigest()

    def __setlogger(self) -> None:
        """
        Add logging support and configure logger.
        """
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel('INFO')
        e_handler = logging.StreamHandler(sys.stdout)
        e_handler.setFormatter(logging.Formatter(HUDSettings.log_stdfmt))
        self.__logger.addHandler(e_handler)

    def __checkdb(self) -> bool:
        """
        Check if specified HUD database file exists.
        :return: Return True if HUD database file exists.
        :rtype: bool
        """
        return os.path.isfile(self.__gamedb)

    def __readdb(self) -> None:
        """
        Read and parse HUD XML database file.
        """
        if not self.__checkdb():
            raise FileNotFoundError(HUDMessages.db_notfound.format(self.__gamedb))

        self.__huddb = xml.dom.minidom.parse(self.__gamedb)
        for hud in self.__huddb.getElementsByTagName('HUD'):
            self.__hudlist.append(HUDEntry(hud))

    def __usegh(self, hud: HUDEntry) -> None:
        """
        Call GitHub and download latest revision of specified HUD.
        :param hud: HUD entry to process and download.
        """
        r = self.callgithubapi(hud.repopath)
        if r[1] > hud.lastupdate:
            f = self.renamefile(self.downloadfile(hud.upstreamuri, hud.installdir, self.__outdir), r[0])
            updatefile = os.path.basename(f)

            hud.mainuri = '{}/{}'.format(os.path.dirname(hud.mainuri), updatefile)
            hud.mirroruri = '{}/{}'.format(os.path.dirname(hud.mirroruri), updatefile)
            hud.sha512hash = self.sha512hash(f)
            hud.lastupdate = r[1]
            hud.isupdated = True

            self.__logger.info(
                HUDMessages.hud_updated.format(hud.hudname, hud.sha512hash, hud.lastupdate, updatefile))
        else:
            if (not hud.isupdated) and (int(time.time()) - hud.lastupdate >= 31536000):
                self.__logger.warning(HUDMessages.hud_outdated.format(hud.hudname))
            else:
                self.__logger.info(HUDMessages.hud_uptodate.format(hud.hudname))

    def __useother(self, hud: HUDEntry) -> None:
        """
        Download specified HUD from unknown location.
        :param hud: HUD entry to process and download.
        """
        mdate = self.hth2unix(self.getlhmurl(hud.upstreamuri))
        if mdate > hud.lastupdate:
            filednl = self.downloadfile(hud.upstreamuri, hud.installdir, self.__outdir)
            fullfile = self.renamefile(filednl, self.sha1hash(filednl))
            updatefile = os.path.basename(fullfile)

            hud.mainuri = '{}/{}'.format(os.path.dirname(hud.mainuri), updatefile)
            hud.mirroruri = '{}/{}'.format(os.path.dirname(hud.mirroruri), updatefile)
            hud.sha512hash = self.sha512hash(fullfile)
            hud.lastupdate = mdate
            hud.isupdated = True

            self.__logger.info(
                HUDMessages.hud_updated.format(hud.hudname, hud.sha512hash, hud.lastupdate, updatefile))
        else:
            if (not hud.isupdated) and (int(time.time()) - hud.lastupdate >= 31536000):
                self.__logger.warning(HUDMessages.hud_outdated.format(hud.hudname))
            else:
                self.__logger.info(HUDMessages.hud_uptodate.format(hud.hudname))

    def __handlehud(self, hud: HUDEntry) -> None:
        """
        Process and download specified HUD using different backends.
        :param hud: HUD entry to process and download.
        """
        if hud.ghhosted:
            self.__usegh(hud)
        else:
            self.__useother(hud)

    def getall(self) -> None:
        """
        Process and download updates for all HUDs from database.
        """
        for hud in self.__hudlist:
            try:
                self.__handlehud(hud)
            except Exception:
                self.__logger.exception(HUDMessages.hud_error.format(hud.hudname))

    def save(self) -> None:
        """
        Save changes back to XML database file.
        """
        with open(self.__gamedb, 'w') as writer:
            self.__huddb.writexml(writer, encoding='utf-8')

    def __init__(self, gamedb: str, outdir: str) -> None:
        """
        Main constructor of HUDMirror class.
        :param gamedb: Full path to game database file.
        :param outdir: Full path to output directory.
        """
        self.__gamedb = gamedb
        self.__outdir = outdir
        self.__hudlist = []
        self.__setlogger()
        self.__readdb()
