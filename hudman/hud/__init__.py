# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import abc
import os

from ..dnmanager import DnManager


class HUDCommon(metaclass=abc.ABCMeta):
    """
    Abstract class for working with HUDs.
    """

    @abc.abstractmethod
    def _updatecheck(self) -> int:
        """
        Fetch an external source and get last modification time of
        the selected HUD. Abstract method.
        :return: Last modification time in unixtime format.
        :rtype: int
        """

    @property
    def hudname(self) -> str:
        """
        Get user friendly HUD name.
        :return: HUD name.
        """
        return self._hudname.data

    @hudname.setter
    def hudname(self, value: str) -> None:
        """
        Set user friendly HUD name.
        """
        self._hudname.data = value

    @property
    def gamename(self) -> str:
        """
        Get HUD's game name.
        :return: Game name.
        """
        return self._gamename.data

    @gamename.setter
    def gamename(self, value: str) -> None:
        """
        Set HUD's game name.
        """
        self._gamename.data = value

    @property
    def isupdated(self) -> bool:
        """
        Check if current HUD is up to date.
        :return: Update result.
        """
        return self._isupdated.data == '1'

    @isupdated.setter
    def isupdated(self, value: bool) -> None:
        """
        Set if current HUD is up to date.
        """
        self._isupdated.data = '1' if value else '0'

    @property
    def mainuri(self) -> str:
        """
        Get local mirror URI.
        :return: Mirror URI.
        """
        return self._mainuri.data

    @mainuri.setter
    def mainuri(self, value: str) -> None:
        """
        Set local mirror URI.
        """
        self._mainuri.data = value

    @property
    def mirroruri(self) -> str:
        """
        Get local secondary server URI.
        :return: Mirror URI.
        """
        return self._mirroruri.data

    @mirroruri.setter
    def mirroruri(self, value: str) -> None:
        """
        Set local secondary server URI.
        """
        self._mirroruri.data = value

    @property
    def upstreamuri(self) -> str:
        """
        Get upstream URI.
        :return: Upstream URI.
        """
        return self._upstreamuri.data

    @upstreamuri.setter
    def upstreamuri(self, value: str) -> None:
        """
        Set upstream URI.
        """
        self._upstreamuri.data = value

    @property
    def screenshoturi(self) -> str:
        """
        Get screenshot URI.
        :return: Screenshot URI.
        """
        return self._screenshot.data

    @screenshoturi.setter
    def screenshoturi(self, value: str) -> None:
        """
        Set screenshot URI.
        """
        self._screenshot.data = value

    @property
    def repopath(self) -> str:
        """
        Get upstream repository URL.
        :return: Upstream repository URL.
        """
        return self._repopath.data

    @repopath.setter
    def repopath(self, value: str) -> None:
        """
        Set upstream repository URL.
        """
        self._repopath.data = value

    @property
    def sha512hash(self) -> str:
        """
        Get SHA-512 hash sum of HUD file.
        :return: SHA-512 hash sum of HUD file.
        """
        return self._sha512hash.data

    @sha512hash.setter
    def sha512hash(self, value: str) -> None:
        """
        Set SHA-512 hash sum of HUD file.
        """
        self._sha512hash.data = value

    @property
    def lastupdate(self) -> int:
        """
        Get last update time in Unixtime format.
        :return: Last update time.
        """
        return int(self._lastupdate.data)

    @lastupdate.setter
    def lastupdate(self, value: int) -> None:
        """
        Set last update time in Unixtime format.
        """
        self._lastupdate.data = str(value)

    @property
    def homepage(self) -> str:
        """
        Get homepage of HUD.
        :return: Homepage of HUD.
        """
        return self._homepage.data

    @homepage.setter
    def homepage(self, value: str) -> None:
        """
        Set homepage of HUD.
        """
        self._homepage.data = value

    @property
    def archivedir(self) -> str:
        """
        Get actual archive dir inside archive.
        :return: Archive directory name.
        """
        return self._archivedir.data

    @archivedir.setter
    def archivedir(self, value: str) -> None:
        """
        Set actual archive dir inside archive.
        """
        self._archivedir.data = value

    @property
    def installdir(self) -> str:
        """
        Get install directory of HUD.
        :return: HUD install directory.
        """
        return self._installdir.data

    @installdir.setter
    def installdir(self, value: str) -> None:
        """
        Set install directory of HUD.
        """
        self._installdir.data = value

    @property
    def filename(self) -> str:
        """
        Get final download filename for HUD.
        :return: Download filename for HUD.
        """
        return os.path.basename(self.mainuri)

    def check(self) -> bool:
        """
        Check for the HUD updates.
        :return: Return True if the new version is available.
        :rtype: bool
        """
        self._checkresult = self._updatecheck()
        return self._checkresult > self.lastupdate

    def download(self, outdir: str) -> bool:
        """
        Download current version of the specified HUD.
        :param outdir: Output directory.
        :return: Return True if the specified HUD was downloaded successfully.
        :rtype: bool
        """
        df = DnManager.downloadfile(self.mainuri, self.installdir, outdir)
        f = DnManager.renamefile(df, self.filename)
        return DnManager.sha512hash(f) == self.sha512hash

    def update(self, outdir: str) -> None:
        """
        Download the latest version of the specified HUD.
        :param outdir: Output directory.
        """
        df = DnManager.downloadfile(self.upstreamuri, self.installdir, outdir)
        f = DnManager.renamefilehash(df, DnManager.sha256hash(df))
        updatefile = os.path.basename(f)

        self.mainuri = '{}/{}'.format(os.path.dirname(self.mainuri), updatefile)
        self.mirroruri = '{}/{}'.format(os.path.dirname(self.mirroruri), updatefile)
        self.sha512hash = DnManager.sha512hash(f)
        self.lastupdate = self._checkresult
        self.isupdated = True

    def __init__(self, hud) -> None:
        """
        Main constructor of HUDEntry class.
        :param hud: A single entry from HUD database.
        """
        self._hudname = hud.getElementsByTagName('Name')[0].firstChild
        self._gamename = hud.getElementsByTagName('Game')[0].firstChild
        self._isupdated = hud.getElementsByTagName('IsUpdated')[0].firstChild
        self._mainuri = hud.getElementsByTagName('URI')[0].firstChild
        self._mirroruri = hud.getElementsByTagName('Mirror')[0].firstChild
        self._upstreamuri = hud.getElementsByTagName('UpURI')[0].firstChild
        self._screenshot = hud.getElementsByTagName('Preview')[0].firstChild
        self._repopath = hud.getElementsByTagName('RepoPath')[0].firstChild
        self._sha512hash = hud.getElementsByTagName('Hash2')[0].firstChild
        self._lastupdate = hud.getElementsByTagName('LastUpdate')[0].firstChild
        self._homepage = hud.getElementsByTagName('Site')[0].firstChild
        self._archivedir = hud.getElementsByTagName('ArchiveDir')[0].firstChild
        self._installdir = hud.getElementsByTagName('InstallDir')[0].firstChild
        self._checkresult = 0
