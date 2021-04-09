# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import hashlib
import os
import urllib.request

from ..hudmsg import HUDSettings


class DnManager:
    @staticmethod
    def downloadfile(url: str, name: str, outdir: str) -> str:
        """
        Download file from Internet and save it to specified directory.
        :param url: URL of remote file.
        :param name: Name of result file.
        :param outdir: Output directory.
        :return: Full local path of downloaded file.
        :rtype: str
        """
        fdir = os.path.join(outdir, name)
        if not os.path.exists(fdir):
            os.makedirs(fdir)
        filepath = os.path.join(fdir, '{}.zip'.format(name))
        request = urllib.request.Request(url, data=None, headers={'User-Agent': HUDSettings.ua_wget})
        with urllib.request.urlopen(request) as response, open(filepath, 'wb') as result:
            result.write(response.read())
        return filepath

    @staticmethod
    def renamefile(fname: str, chash: str) -> str:
        """
        Rename file using it's hash.
        :param fname: Source file name.
        :param chash: Source file hash sum.
        :return: Full local path of renamed file.
        :rtype: str
        """
        fdir = os.path.dirname(fname)
        result = os.path.join(fdir, '{}_{}.zip'.format(os.path.splitext(os.path.basename(fname))[0], chash[:8]))
        if os.path.isfile(result):
            os.remove(result)
        os.rename(fname, result)
        return result

    @staticmethod
    def sha256hash(fname: str) -> str:
        """
        Calculate SHA-256 hash sum of specified file.
        :param fname: Source file name.
        :return: SHA1 hash of source file.
        :rtype: str
        """
        return hashlib.sha256(open(fname, 'rb').read()).hexdigest()

    @staticmethod
    def sha512hash(fname: str) -> str:
        """
        Calculate SHA-512 hash sum of specified file.
        :param fname: Source file name.
        :return: SHA-512 hash of source file.
        :rtype: str
        """
        return hashlib.sha512(open(fname, 'rb').read()).hexdigest()