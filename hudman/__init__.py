#!/usr/bin/python3
# coding=utf-8

#
# This file is a part of HUD mirror script. For more information
# visit official site: https://www.easycoding.org/projects/hudman
#
# Copyright (c) 2016 - 2018 EasyCoding Team.
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
#

from .hudlist import HUDEntry
from os import path, makedirs, rename
from xml.dom import minidom
from datetime import datetime
from calendar import timegm
from hashlib import md5, sha1
from json import loads
from urllib.request import Request, urlopen


class HUDMirror:
    @staticmethod
    def gmt2unix(gtime: str) -> int:
        do = datetime.strptime(gtime, '%Y-%m-%dT%H:%M:%SZ')
        return int(timegm(do.timetuple()))

    @staticmethod
    def callgithubapi(repourl):
        url = repourl.replace('https://github.com/', 'https://api.github.com/repos/') + '/commits?per_page=1'
        response = urlopen(Request(url, data=None, headers={'User-Agent': 'curl'}))
        if response.status != 200:
            raise Exception('GitHub API returned %d error code.' % response.status)
        data = loads(response.read().decode('utf-8'))
        return [data[0]['sha'], HUDMirror.gmt2unix(data[0]['commit']['committer']['date'])]

    @staticmethod
    def downloadfile(outdir: str, url: str, name: str) -> str:
        fdir = path.join(outdir, name)
        if not path.exists(fdir):
            makedirs(fdir)
        filepath = path.join(fdir, '%s.zip' % name)
        with urlopen(url) as response, open(filepath, 'wb') as result:
            result.write(response.read())
        return filepath

    @staticmethod
    def renamefile(fname: str, chash: str) -> str:
        fdir = path.dirname(fname)
        result = path.join(fdir, '%s_%s.zip' % (path.splitext(path.basename(fname))[0], chash[:8]))
        rename(fname, result)
        return result

    @staticmethod
    def md5hash(fname: str) -> str:
        return md5(open(fname, 'rb').read()).hexdigest()

    @staticmethod
    def sha1hash(fname: str) -> str:
        return sha1(open(fname, 'rb').read()).hexdigest()

    def __checkdb(self) -> bool:
        return path.isfile(self.__gamedb)

    def __readdb(self):
        if not self.__checkdb():
            raise FileNotFoundError("Game database file not found: %s." % self.__gamedb)

        huddb = minidom.parse(self.__gamedb)
        for hud in huddb.getElementsByTagName('HUD'):
            self.__hudlist.append(HUDEntry(hud.getElementsByTagName("Name")[0].firstChild.data,
                                           hud.getElementsByTagName("InstallDir")[0].firstChild.data,
                                           hud.getElementsByTagName("UpURI")[0].firstChild.data,
                                           hud.getElementsByTagName("RepoPath")[0].firstChild.data,
                                           hud.getElementsByTagName("LastUpdate")[0].firstChild.data,
                                           hud.getElementsByTagName("URI")[0].firstChild.data))

    def __init__(self, gamedb, outdir):
        self.__gamedb = gamedb
        self.__outdir = outdir
        self.__hudlist = []
        self.__readdb()
