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
    def installdir(self) -> str:
        """
        Get install directory of HUD.
        :return: HUD install directory.
        """
        return self.__installdir

    @property
    def upstreamuri(self) -> str:
        """
        Get upstream URI.
        :return: Upstream URI.
        """
        return self.__upstreamuri

    @property
    def repopath(self) -> str:
        """
        Get upstream repository URL.
        :return: Upstream repository URL.
        """
        return self.__repopath

    @property
    def lastupdate(self) -> int:
        """
        Get last update time in Unixtime format.
        :return: Last update time.
        """
        return self.__lastupdate

    @property
    def filename(self) -> str:
        """
        Get final download filename for HUD.
        :return: Download filename for HUD.
        """
        return self.__filename

    @property
    def ghhosted(self) -> bool:
        """
        Check if HUD hosted on GitHub.
        :return: Return True if HUD hosted on GitHub.
        """
        return self.__repopath.find('https://github.com/') != -1

    def __init__(self, hudname: str, gamename: str, isupdated: str, mirroruri: str,
                 upstreamuri: str, screenshot: str, repopath: str, hashsum: str,
                 lastupdate: str, homepage: str, archivedir: str, installdir: str,
                 filename: str) -> None:
        """
        Main constructor of HUDEntry class.
        :param hudname: Value of InstallDir value from HUD database.
        :param upstreamuri: Value of UpURI value from HUD database.
        :param repopath: Value of RepoPath value from HUD database.
        :param lastupdate: Value of LastUpdate value from HUD database.
        :param filename: Value of URI value from HUD database.
        """
        self.__hudname = hudname
        self.__gamename = gamename
        self.__isupdated = isupdated == 1
        self.__mirroruri = mirroruri
        self.__upstreamuri = upstreamuri
        self.__screenshot = screenshot
        self.__repopath = repopath
        self.__hashsum = hashsum
        self.__lastupdate = int(lastupdate)
        self.__homepage = homepage
        self.__archivedir = archivedir
        self.__installdir = installdir
        self.__filename = path.basename(filename)
