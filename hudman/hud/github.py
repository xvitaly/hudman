# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import base64
import json
import requests

from ..headertime import HeaderTime
from ..hud import HUDCommon
from ..settings import Settings


class HUDGitHub(HUDCommon):
    """
    Class for working with HUDs hosted on GitHub.
    """

    def _updatecheck(self) -> int:
        """
        Call GitHub API and fetch last modification time of the
        specified HUD.
        :return: Last modification time in the unixtime format.
        :rtype: int
        """
        headers = {'User-Agent': Settings.apifetch_user_agent}
        if self._ghuser and self._ghtoken:
            auth = base64.b64encode(f'{self._ghuser}:{self._ghtoken}'.encode('ascii'))
            headers['Authorization'] = f'Basic {auth.decode("ascii")}'
        response = requests.get(self._apiurl, allow_redirects=True, headers=headers)
        response.raise_for_status()
        return HeaderTime.gmt2unix(json.loads(response.content)[0]['commit']['committer']['date'])

    def __init__(self, hud):
        """
        Main constructor of the HUDGitHub class.
        :param hud: A single entry from the HUD database.
        """
        super().__init__(hud)
        self._apiurl = self.repopath.replace('https://github.com/',
                                             'https://api.github.com/repos/') + '/commits?per_page=1'
        self._ghuser = Settings.github_user
        self._ghtoken = Settings.github_token
