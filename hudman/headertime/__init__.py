# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import calendar
import datetime
import email.utils


class HeaderTime:
    @staticmethod
    def gmt2unix(gtime: str) -> int:
        """
        Convert datetime string to unixtime.
        :param gtime: Datetime string.
        :return: UnixTime integer.
        :rtype: int
        """
        do = datetime.datetime.strptime(gtime, '%Y-%m-%dT%H:%M:%SZ')
        return int(calendar.timegm(do.timetuple()))

    @staticmethod
    def hth2unix(gtime: str) -> int:
        """
        Convert datetime string in HTTP-header format to unixtime.
        :param gtime: Datetime string in HTTP-header format.
        :return: UnixTime integer.
        :rtype: int
        """
        return int(calendar.timegm(email.utils.parsedate(gtime)))
