# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import requests

from ...headertime import HeaderTime
from ...hud import HUDCommon
from ...messages import Messages
from ...settings import Settings


class HUDOther(HUDCommon):
    """
    Class for working with HUDs stored on any other file
    hostings.
    """
    def _updatecheck(self) -> int:
        """
        Call HTTP HEAD method to retrieve last modification time
        of specified URL.
        :return: Last modification time in the unixtime format.
        :rtype: int
        """
        response = requests.head(self.upstreamuri, headers={'User-Agent': Settings.apifetch_user_agent})
        if response.status_code != 200:
            raise Exception(Messages.oth_errcode.format(response.status_code))
        return HeaderTime.hth2unix(response.headers['Last-Modified'])

    def download(self, outdir: str) -> None:
        """
        Download the latest version of the specified HUD.
        :param outdir: Output directory.
        """
        super().download(outdir)
        self.mainuri = self.upstreamuri
