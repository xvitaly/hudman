# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import urllib.request

from ...headertime import HeaderTime
from ...hud import HUDCommon
from ...hudmsg import HUDMessages
from ...settings import Settings


class HUDOther(HUDCommon):
    def _updatecheck(self) -> int:
        """
        Call HTTP HEAD method to retrieve last modification time
        of specified URL.
        :return: Last modification time in unixtime format.
        :rtype: int
        """
        request = urllib.request.Request(self.upstreamuri, data=None,
                                         headers={'User-Agent': Settings.apifetch_user_agent}, method='HEAD')
        response = urllib.request.urlopen(request)
        if response.status != 200:
            raise Exception(HUDMessages.oth_errcode.format(response.status))
        headers = response.info()
        return HeaderTime.hth2unix(headers['Last-Modified'])
