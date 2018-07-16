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

from os import path


class HUDEntry:
    @property
    def hudname(self) -> str:
        """
        Get user friendly HUD name.
        :return: HUD name.
        """
        return self.__hudname

    @property
    def gamename(self) -> str:
        """
        Get HUD's game name.
        :return: Game name.
        """
        return self.__gamename

    @property
    def isupdated(self) -> bool:
        """
        Checks if current HUD is up to date.
        :return: Update result.
        """
        return self.__isupdated == '1'

    @property
    def mirroruri(self) -> str:
        """
        Get local mirror URI.
        :return: Mirror URI.
        """
        return self.__mirroruri

    @property
    def upstreamuri(self) -> str:
        """
        Get upstream URI.
        :return: Upstream URI.
        """
        return self.__upstreamuri

    @property
    def screenshoturi(self) -> str:
        """
        Get screenshot URI.
        :return: Screenshot URI.
        """
        return self.__screenshot

    @property
    def repopath(self) -> str:
        """
        Get upstream repository URL.
        :return: Upstream repository URL.
        """
        return self.__repopath

    @property
    def hashsum(self) -> str:
        """
        Get hash sum of HUD.
        :return: Hash sum of HUD.
        """
        return self.__hashsum

    @property
    def lastupdate(self) -> int:
        """
        Get last update time in Unixtime format.
        :return: Last update time.
        """
        return int(self.__lastupdate)

    @property
    def homepage(self) -> str:
        """
        Get homepage of HUD.
        :return: Homepage of HUD.
        """
        return self.__homepage

    @property
    def archivedir(self) -> str:
        """
        Get actual archive dir inside archive.
        :return: Archive directory name.
        """
        return self.__archivedir

    @property
    def installdir(self) -> str:
        """
        Get install directory of HUD.
        :return: HUD install directory.
        """
        return self.__installdir

    @property
    def filename(self) -> str:
        """
        Get final download filename for HUD.
        :return: Download filename for HUD.
        """
        return path.basename(self.__mirroruri)

    @property
    def ghhosted(self) -> bool:
        """
        Check if HUD hosted on GitHub.
        :return: Return True if HUD hosted on GitHub.
        """
        return self.__repopath.find('https://github.com/') != -1

    def __init__(self, hudname: str, gamename: str, isupdated: str, mirroruri: str,
                 upstreamuri: str, screenshot: str, repopath: str, hashsum: str,
                 lastupdate: str, homepage: str, archivedir: str, installdir: str) -> None:
        """
        Main constructor of HUDEntry class.
        :param hudname: Value of Name value from HUD database.
        :param gamename: Value of Game value from HUD database.
        :param isupdated: Value of IsUpdated value from HUD database.
        :param mirroruri: Value of URI value from HUD database.
        :param upstreamuri: Value of UpURI value from HUD database.
        :param screenshot: Value of Preview value from HUD database.
        :param repopath: Value of RepoPath value from HUD database.
        :param hashsum: Value of Hash value from HUD database.
        :param lastupdate: Value of LastUpdate value from HUD database.
        :param homepage: Value of Site value from HUD database.
        :param archivedir: Value of ArchiveDir value from HUD database.
        :param installdir: Value of InstallDir value from HUD database.
        """
        self.__hudname = hudname
        self.__gamename = gamename
        self.__isupdated = isupdated
        self.__mirroruri = mirroruri
        self.__upstreamuri = upstreamuri
        self.__screenshot = screenshot
        self.__repopath = repopath
        self.__hashsum = hashsum
        self.__lastupdate = lastupdate
        self.__homepage = homepage
        self.__archivedir = archivedir
        self.__installdir = installdir
