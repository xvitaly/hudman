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
from os import path
from xml.dom import minidom


class HUDMirror:
    def __checkdb(self) -> bool:
        return path.isfile(self.__gamedb)

    def __readdb(self):
        if not self.__checkdb():
            raise Exception("Game database file not found: %s." % self.__gamedb)

        huddb = minidom.parse(self.__gamedb)
        for hud in huddb.getElementsByTagName('HUD'):
            self.__hudlist.append(HUDEntry(hud.getElementsByTagName("Name")[0].firstChild.data,
                                           hud.getElementsByTagName("InstallDir")[0].firstChild.data,
                                           hud.getElementsByTagName("UpURI")[0].firstChild.data,
                                           hud.getElementsByTagName("RepoPath")[0].firstChild.data,
                                           hud.getElementsByTagName("LastUpdate")[0].firstChild.data,
                                           hud.getElementsByTagName("URI")[0].firstChild.data))

    def __init__(self, gamedb):
        self.__gamedb = gamedb
        self.__hudlist = []
        self.__readdb()
