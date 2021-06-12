# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ..github import HUDGitHub
from ..other import HUDOther


class HUDFactory:
    """
    Static class with factory methods.
    """

    @staticmethod
    def create(hud):
        """
        Get the correct instance of the HUD manager. Factory method.
        :param hud: Specified HUD entry.
        :return: An instance of the desired class.
        :rtype: Any
        """
        repopath = hud.getElementsByTagName('RepoPath')[0].firstChild.data
        return HUDGitHub(hud) if repopath.find('https://github.com/') != -1 else HUDOther(hud)
