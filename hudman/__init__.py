# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import os
import time

import defusedxml.minidom

from .hud.factory import HUDFactory
from .messages import Messages


class HUDManager:
    """
    Main class for working with the HUD database.
    """

    def __setlogger(self) -> None:
        """
        Add logging support and configure logger.
        """
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)

    def __checkdb(self) -> bool:
        """
        Check if specified HUD database file exists.
        :return: Return True if HUD database file exists.
        :rtype: bool
        """
        return os.path.isfile(self.__gamedb)

    def __readdb(self) -> None:
        """
        Read and parse HUD XML database file.
        """
        if not self.__checkdb():
            raise FileNotFoundError(Messages.db_notfound.format(self.__gamedb))

        self.__huddb = defusedxml.minidom.parse(self.__gamedb)
        for hud in self.__huddb.getElementsByTagName('HUD'):
            self.__hudlist.append(HUDFactory.create(hud))

    def __downloadhud(self, hud) -> None:
        """
        Download specified HUD using different backends without doing
        update.
        :param hud: HUD entry to process and download.
        """
        if hud.download(self.__outdir):
            self.__logger.info(
                Messages.hud_downloaded.format(hud.hudname, hud.sha512hash, hud.lastupdate, hud.filename))
        else:
            self.__logger.warning(Messages.hud_hash_missmatch.format(hud.hudname))

    def __updatehud(self, hud) -> None:
        """
        Process and download specified HUD using different backends.
        :param hud: HUD entry to process and download.
        """
        if hud.check():
            hud.update(self.__outdir)
            self.__logger.info(
                Messages.hud_updated.format(hud.hudname, hud.sha512hash, hud.lastupdate, hud.filename))
        else:
            if (not hud.isupdated) and (int(time.time()) - hud.lastupdate >= 31536000):
                self.__logger.warning(Messages.hud_outdated.format(hud.hudname))
            else:
                self.__logger.info(Messages.hud_uptodate.format(hud.hudname))

    def getall(self) -> None:
        """
        Downloads all HUDs from the database.
        """
        for hud in self.__hudlist:
            try:
                self.__downloadhud(hud)
            except Exception:
                self.__logger.exception(Messages.hud_error.format(hud.hudname))

    def updateall(self) -> None:
        """
        Process and download updates for all HUDs from the database.
        """
        for hud in self.__hudlist:
            try:
                self.__updatehud(hud)
            except Exception:
                self.__logger.exception(Messages.hud_error.format(hud.hudname))

    def save(self) -> None:
        """
        Save changes back to XML database file.
        """
        with open(self.__gamedb, 'w') as writer:
            self.__huddb.writexml(writer, encoding='utf-8')

    def __init__(self, gamedb: str, outdir: str) -> None:
        """
        Main constructor of HUDManager class.
        :param gamedb: Full path to game database file.
        :param outdir: Full path to output directory.
        """
        self.__gamedb = gamedb
        self.__outdir = outdir
        self.__hudlist = []
        self.__setlogger()
        self.__readdb()
