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

from os import path


class HUDEntry:
    @property
    def hudname(self) -> str:
        """
        Get user friendly HUD name.
        :return: HUD name.
        """
        return self.__hudname.data

    @hudname.setter
    def hudname(self, value: str) -> None:
        """
        Set user friendly HUD name.
        """
        self.__hudname.data = value

    @property
    def gamename(self) -> str:
        """
        Get HUD's game name.
        :return: Game name.
        """
        return self.__gamename.data

    @gamename.setter
    def gamename(self, value: str) -> None:
        """
        Set HUD's game name.
        """
        self.__gamename.data = value

    @property
    def isupdated(self) -> bool:
        """
        Check if current HUD is up to date.
        :return: Update result.
        """
        return self.__isupdated.data == '1'

    @isupdated.setter
    def isupdated(self, value: bool) -> None:
        """
        Set if current HUD is up to date.
        """
        self.__isupdated.data = '1' if value else '0'

    @property
    def mirroruri(self) -> str:
        """
        Get local mirror URI.
        :return: Mirror URI.
        """
        return self.__mirroruri.data

    @mirroruri.setter
    def mirroruri(self, value: str) -> None:
        """
        Set local mirror URI.
        """
        self.__mirroruri.data = value

    @property
    def upstreamuri(self) -> str:
        """
        Get upstream URI.
        :return: Upstream URI.
        """
        return self.__upstreamuri.data

    @upstreamuri.setter
    def upstreamuri(self, value: str) -> None:
        """
        Set upstream URI.
        """
        self.__upstreamuri.data = value

    @property
    def screenshoturi(self) -> str:
        """
        Get screenshot URI.
        :return: Screenshot URI.
        """
        return self.__screenshot.data

    @screenshoturi.setter
    def screenshoturi(self, value: str) -> None:
        """
        Set screenshot URI.
        """
        self.__screenshot.data = value

    @property
    def repopath(self) -> str:
        """
        Get upstream repository URL.
        :return: Upstream repository URL.
        """
        return self.__repopath.data

    @repopath.setter
    def repopath(self, value: str) -> None:
        """
        Set upstream repository URL.
        """
        self.__repopath.data = value

    @property
    def md5hash(self) -> str:
        """
        Get MD5 hash sum of HUD file.
        :return: MD5 hash sum of HUD file.
        """
        return self.__md5hash.data

    @md5hash.setter
    def md5hash(self, value: str) -> None:
        """
        Set MD5 hash sum of HUD file.
        """
        self.__md5hash.data = value

    @property
    def lastupdate(self) -> int:
        """
        Get last update time in Unixtime format.
        :return: Last update time.
        """
        return int(self.__lastupdate.data)

    @lastupdate.setter
    def lastupdate(self, value: int) -> None:
        """
        Set last update time in Unixtime format.
        """
        self.__lastupdate.data = str(value)

    @property
    def homepage(self) -> str:
        """
        Get homepage of HUD.
        :return: Homepage of HUD.
        """
        return self.__homepage.data

    @homepage.setter
    def homepage(self, value: str) -> None:
        """
        Set homepage of HUD.
        """
        self.__homepage.data = value

    @property
    def archivedir(self) -> str:
        """
        Get actual archive dir inside archive.
        :return: Archive directory name.
        """
        return self.__archivedir.data

    @archivedir.setter
    def archivedir(self, value: str) -> None:
        """
        Set actual archive dir inside archive.
        """
        self.__archivedir.data = value

    @property
    def installdir(self) -> str:
        """
        Get install directory of HUD.
        :return: HUD install directory.
        """
        return self.__installdir.data

    @installdir.setter
    def installdir(self, value: str) -> None:
        """
        Set install directory of HUD.
        """
        self.__installdir.data = value

    @property
    def filename(self) -> str:
        """
        Get final download filename for HUD.
        :return: Download filename for HUD.
        """
        return path.basename(self.mirroruri)

    @property
    def ghhosted(self) -> bool:
        """
        Check if HUD hosted on GitHub.
        :return: Return True if HUD hosted on GitHub.
        """
        return self.repopath.find('https://github.com/') != -1

    def __init__(self, hud) -> None:
        """
        Main constructor of HUDEntry class.
        :param hud: A single entry from HUD database.
        """
        self.__hudname = hud.getElementsByTagName('Name')[0].firstChild
        self.__gamename = hud.getElementsByTagName('Game')[0].firstChild
        self.__isupdated = hud.getElementsByTagName('IsUpdated')[0].firstChild
        self.__mirroruri = hud.getElementsByTagName('URI')[0].firstChild
        self.__upstreamuri = hud.getElementsByTagName('UpURI')[0].firstChild
        self.__screenshot = hud.getElementsByTagName('Preview')[0].firstChild
        self.__repopath = hud.getElementsByTagName('RepoPath')[0].firstChild
        self.__md5hash = hud.getElementsByTagName('Hash')[0].firstChild
        self.__sha512hash = hud.getElementsByTagName('Hash2')[0].firstChild
        self.__lastupdate = hud.getElementsByTagName('LastUpdate')[0].firstChild
        self.__homepage = hud.getElementsByTagName('Site')[0].firstChild
        self.__archivedir = hud.getElementsByTagName('ArchiveDir')[0].firstChild
        self.__installdir = hud.getElementsByTagName('InstallDir')[0].firstChild
