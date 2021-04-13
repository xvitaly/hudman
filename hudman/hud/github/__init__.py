# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import base64
import json
import urllib.request

from ...headertime import HeaderTime
from ...hud import HUDCommon
from ...messages import Messages
from ...settings import Settings


class HUDGitHub(HUDCommon):
    def _updatecheck(self) -> int:
        """
        Call GitHub API and fetch last modification time of the
        specified HUD.
        :return: Last modification time in unixtime format.
        :rtype: int
        """
        request = urllib.request.Request(self.__apiurl, data=None, headers={'User-Agent': Settings.apifetch_user_agent})
        if self.__ghuser and self.__ghtoken:
            auth = base64.b64encode(f'{self.__ghuser}:{self.__ghtoken}'.encode('ascii'))
            request.add_header('Authorization', f'Basic {auth.decode("ascii")}')
        response = urllib.request.urlopen(request)
        if response.status != 200:
            raise Exception(Messages.gh_errcode.format(response.status))
        data = json.loads(response.read().decode('utf-8'))
        return HeaderTime.gmt2unix(data[0]['commit']['committer']['date'])

    def __init__(self, hud):
        """
        Main constructor of the HUDGitHub class.
        :param hud: A single entry from HUD database.
        """
        super().__init__(hud)
        self.__apiurl = self.repopath.replace('https://github.com/',
                                              'https://api.github.com/repos/') + '/commits?per_page=1'
        self.__ghuser = Settings.github_user
        self.__ghtoken = Settings.github_token
