# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
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
        return self.__hudname.data

    @hudname.setter
    def hudname(self, value: str) -> None:
        """
        Set user friendly HUD name.
        """
        self.__hudname.data = value

    @property
    def gamename(self) -> str:
        """
        Get HUD's game name.
        :return: Game name.
        """
        return self.__gamename.data

    @gamename.setter
    def gamename(self, value: str) -> None:
        """
        Set HUD's game name.
        """
        self.__gamename.data = value

    @property
    def isupdated(self) -> bool:
        """
        Check if current HUD is up to date.
        :return: Update result.
        """
        return self.__isupdated.data == '1'

    @isupdated.setter
    def isupdated(self, value: bool) -> None:
        """
        Set if current HUD is up to date.
        """
        self.__isupdated.data = '1' if value else '0'

    @property
    def mainuri(self) -> str:
        """
        Get local mirror URI.
        :return: Mirror URI.
        """
        return self.__mainuri.data

    @mainuri.setter
    def mainuri(self, value: str) -> None:
        """
        Set local mirror URI.
        """
        self.__mainuri.data = value

    @property
    def mirroruri(self) -> str:
        """
        Get local secondary server URI.
        :return: Mirror URI.
        """
        return self.__mirroruri.data

    @mirroruri.setter
    def mirroruri(self, value: str) -> None:
        """
        Set local secondary server URI.
        """
        self.__mirroruri.data = value

    @property
    def upstreamuri(self) -> str:
        """
        Get upstream URI.
        :return: Upstream URI.
        """
        return self.__upstreamuri.data

    @upstreamuri.setter
    def upstreamuri(self, value: str) -> None:
        """
        Set upstream URI.
        """
        self.__upstreamuri.data = value

    @property
    def screenshoturi(self) -> str:
        """
        Get screenshot URI.
        :return: Screenshot URI.
        """
        return self.__screenshot.data

    @screenshoturi.setter
    def screenshoturi(self, value: str) -> None:
        """
        Set screenshot URI.
        """
        self.__screenshot.data = value

    @property
    def repopath(self) -> str:
        """
        Get upstream repository URL.
        :return: Upstream repository URL.
        """
        return self.__repopath.data

    @repopath.setter
    def repopath(self, value: str) -> None:
        """
        Set upstream repository URL.
        """
        self.__repopath.data = value

    @property
    def sha512hash(self) -> str:
        """
        Get SHA-512 hash sum of HUD file.
        :return: SHA-512 hash sum of HUD file.
        """
        return self.__sha512hash.data

    @sha512hash.setter
    def sha512hash(self, value: str) -> None:
        """
        Set SHA-512 hash sum of HUD file.
        """
        self.__sha512hash.data = value

    @property
    def lastupdate(self) -> int:
        """
        Get last update time in Unixtime format.
        :return: Last update time.
        """
        return int(self.__lastupdate.data)

    @lastupdate.setter
    def lastupdate(self, value: int) -> None:
        """
        Set last update time in Unixtime format.
        """
        self.__lastupdate.data = str(value)

    @property
    def homepage(self) -> str:
        """
        Get homepage of HUD.
        :return: Homepage of HUD.
        """
        return self.__homepage.data

    @homepage.setter
    def homepage(self, value: str) -> None:
        """
        Set homepage of HUD.
        """
        self.__homepage.data = value

    @property
    def archivedir(self) -> str:
        """
        Get actual archive dir inside archive.
        :return: Archive directory name.
        """
        return self.__archivedir.data

    @archivedir.setter
    def archivedir(self, value: str) -> None:
        """
        Set actual archive dir inside archive.
        """
        self.__archivedir.data = value

    @property
    def installdir(self) -> str:
        """
        Get install directory of HUD.
        :return: HUD install directory.
        """
        return self.__installdir.data

    @installdir.setter
    def installdir(self, value: str) -> None:
        """
        Set install directory of HUD.
        """
        self.__installdir.data = value

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
        self.__checkresult = self._updatecheck()
        return self.__checkresult > self.lastupdate

    def download(self, outdir: str) -> None:
        """
        Download the latest version of the specified HUD.
        :param outdir: Output directory.
        """
        df = DnManager.downloadfile(self.upstreamuri, self.installdir, outdir)
        f = DnManager.renamefile(df, DnManager.sha256hash(df))
        updatefile = os.path.basename(f)

        self.mainuri = '{}/{}'.format(os.path.dirname(self.mainuri), updatefile)
        self.mirroruri = '{}/{}'.format(os.path.dirname(self.mirroruri), updatefile)
        self.sha512hash = DnManager.sha512hash(f)
        self.lastupdate = self.__checkresult
        self.isupdated = True

    def __init__(self, hud) -> None:
        """
        Main constructor of HUDEntry class.
        :param hud: A single entry from HUD database.
        """
        self.__hudname = hud.getElementsByTagName('Name')[0].firstChild
        self.__gamename = hud.getElementsByTagName('Game')[0].firstChild
        self.__isupdated = hud.getElementsByTagName('IsUpdated')[0].firstChild
        self.__mainuri = hud.getElementsByTagName('URI')[0].firstChild
        self.__mirroruri = hud.getElementsByTagName('Mirror')[0].firstChild
        self.__upstreamuri = hud.getElementsByTagName('UpURI')[0].firstChild
        self.__screenshot = hud.getElementsByTagName('Preview')[0].firstChild
        self.__repopath = hud.getElementsByTagName('RepoPath')[0].firstChild
        self.__sha512hash = hud.getElementsByTagName('Hash2')[0].firstChild
        self.__lastupdate = hud.getElementsByTagName('LastUpdate')[0].firstChild
        self.__homepage = hud.getElementsByTagName('Site')[0].firstChild
        self.__archivedir = hud.getElementsByTagName('ArchiveDir')[0].firstChild
        self.__installdir = hud.getElementsByTagName('InstallDir')[0].firstChild
        self.__checkresult = 0
