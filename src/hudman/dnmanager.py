# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import hashlib
import os
import requests
import zipfile

from .exceptions import ArchiveNotValid
from .settings import Settings


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
        filepath = os.path.join(fdir, f'{name}.zip')
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
        return DnManager.renamefile(fname, f'{os.path.splitext(os.path.basename(fname))[0]}_{chash[:8]}.zip')

    @staticmethod
    def findarchivedir(fname: str, archivedir: str) -> str:
        """
        Open downloaded archive and find the base directory with HUD files.
        :param fname: Archive file name.
        :param archivedir: Current directory path.
        :exception ArchiveNotValid: Downloaded archive validation failed.
        :return: Base directory relative path.
        :rtype: str
        """
        with zipfile.ZipFile(fname) as archive:
            flist = list(item for item in archive.namelist() if 'info.vdf' in item)
        if not flist:
            raise ArchiveNotValid(f'Cannot find the info.vdf file. {fname} is not a valid HUD archive.')
        if f'{archivedir}/info.vdf' in flist:
            return archivedir
        return os.path.dirname(flist[0])

    @staticmethod
    def findrealurl(url: str, depth: int = 5) -> str:
        """
        Recursively follow redirects and find the real URL.
        :param url: Current URL.
        :param depth: Maximum recursion depth.
        :return: URL after the all redirects.
        :rtype: str
        """
        headers = {'User-Agent': Settings.apifetch_user_agent}
        with requests.head(url, allow_redirects=False, headers=headers) as response:
            if response.is_redirect and depth > 0:
                return DnManager.findrealurl(response.next.url, depth - 1)
        return url

    @staticmethod
    def sha256hash(fname: str) -> str:
        """
        Calculate SHA-256 hash sum of the specified file.
        :param fname: Source file name.
        :return: SHA1 hash of the source file.
        :rtype: str
        """
        with open(fname, 'rb') as f:
            result = hashlib.sha256(f.read()).hexdigest()
        return result

    @staticmethod
    def sha512hash(fname: str) -> str:
        """
        Calculate SHA-512 hash sum of the specified file.
        :param fname: Source file name.
        :return: SHA-512 hash of the source file.
        :rtype: str
        """
        with open(fname, 'rb') as f:
            result = hashlib.sha512(f.read()).hexdigest()
        return result
