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
        Get or set name of HUD.
        :return: HUD name.
        """
        return self.__hudname

    @property
    def upstreamuri(self) -> str:
        return self.__upstreamuri

    @property
    def repopath(self) -> str:
        return self.__repopath

    @property
    def lastupdate(self) -> int:
        return self.__lastupdate

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def ghhosted(self) -> bool:
        return self.__repopath.find('https://github.com/') != -1

    def __init__(self, hudname: str, upstreamuri: str, repopath: str, lastupdate: str, filename: str) -> None:
        self.__hudname = hudname
        self.__upstreamuri = upstreamuri
        self.__repopath = repopath
        self.__lastupdate = int(lastupdate)
        self.__filename = path.basename(filename)
