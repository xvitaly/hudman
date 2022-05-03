# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import hashlib
import os
import uuid
import requests

from ..settings import Settings


class DnManager:
    """
    Static class with methods for working with HUD downloads.
    """

    @staticmethod
    def downloadfile(url: str, name: str, outdir: str) -> str:
        """
        Download HUD archive file from the Internet and save it to the specified
        directory.
        :param url: URL of the remote file.
        :param name: HUD directory name.
        :param outdir: Output directory.
        :return: Full local path of the downloaded file.
        :rtype: str
        """
        fdir = os.path.join(outdir, name)
        if not os.path.exists(fdir):
            os.makedirs(fdir)
        filepath = os.path.join(fdir, '{}.zip'.format(uuid.uuid4()))
        headers = {'User-Agent': Settings.download_user_agent}
        with requests.get(url, allow_redirects=True, headers=headers) as response, open(filepath, 'wb') as result:
            response.raise_for_status()
            result.write(response.content)
        return filepath

    @staticmethod
    def renamefile(fname: str, nfname: str) -> str:
        """
        Rename file with specified name.
        :param fname: Full path to the source file.
        :param nfname: New file name.
        :return: Full local path of the renamed file.
        :rtype: str
        """
        fdir = os.path.dirname(fname)
        result = os.path.join(fdir, nfname)
        if os.path.isfile(result):
            os.remove(result)
        os.rename(fname, result)
        return result

    @staticmethod
    def renamefilehash(fname: str, chash: str) -> str:
        """
        Rename file using its hash.
        :param fname: Source file name.
        :param chash: Source file hash sum.
        :return: Full local path of the renamed file.
        :rtype: str
        """
        return DnManager.renamefile(fname, '{}_{}.zip'.format(os.path.splitext(os.path.basename(fname))[0], chash[:8]))

    @staticmethod
    def sha256hash(fname: str) -> str:
        """
        Calculate SHA-256 hash sum of the specified file.
        :param fname: Source file name.
        :return: SHA1 hash of the source file.
        :rtype: str
        """
        return hashlib.sha256(open(fname, 'rb').read()).hexdigest()

    @staticmethod
    def sha512hash(fname: str) -> str:
        """
        Calculate SHA-512 hash sum of the specified file.
        :param fname: Source file name.
        :return: SHA-512 hash of the source file.
        :rtype: str
        """
        return hashlib.sha512(open(fname, 'rb').read()).hexdigest()
