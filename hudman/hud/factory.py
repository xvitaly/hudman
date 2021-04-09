# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .gh import HUDGh
from .other import HUDOther


class HUDFactory:
    @staticmethod
    def create(hud):
        repopath = hud.getElementsByTagName('RepoPath')[0].firstChild.data
        return HUDGh(hud) if repopath.find('https://github.com/') != -1 else HUDOther(hud)
