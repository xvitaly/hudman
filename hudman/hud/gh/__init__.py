# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import urllib.request

from ...headertime import HeaderTime
from ...hud import HUDCommon
from ...hudmsg import HUDMessages, HUDSettings


class HUDGh(HUDCommon):
    def __callapi(self) -> int:
        """
        Call GitHub API and fetch useful information about project.
        :return: List with SHA1 hash and datetime of latest commit.
        :rtype: int
        """
        url = self.repopath.replace('https://github.com/', 'https://api.github.com/repos/') + '/commits?per_page=1'
        response = urllib.request.urlopen(
            urllib.request.Request(url, data=None, headers={'User-Agent': HUDSettings.ua_curl}))
        if response.status != 200:
            raise Exception(HUDMessages.gh_errcode.format(response.status))
        data = json.loads(response.read().decode('utf-8'))
        return HeaderTime.gmt2unix(data[0]['commit']['committer']['date'])

    def check(self):
        self._updatecheck = self.__callapi()
        return self._updatecheck > self.lastupdate
