# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import logging

from hudman import HUDManager


class App:
    def __setlogger(self) -> None:
        """
        Configure logger for the internal use.
        """
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)

    def __parser_create(self) -> None:
        """
        Create an instance of the command-line arguments parser.
        """
        self.__parser = argparse.ArgumentParser()
        self.__parser_add_arguments()

    def __parser_add_arguments(self) -> None:
        """
        Add new options to the command-line arguments parser.
        """
        self.__parser.add_argument('--huddb', '-d', help='Specify path to HUDs database file.', required=True)
        self.__parser.add_argument('--outdir', '-o', help='Specify path to save downloaded files.', required=True)
        self.__parser.add_argument('--save', '-s', help='Automatically save changes in HUD database file.',
                                   action='store_true', required=False)

    def __parse_arguments(self) -> None:
        """
        Parse the command-line arguments and provides a special object
        to work with.
        """
        self.__arguments = self.__parser.parse_args()

    def run(self) -> None:
        """
        Run the application.
        """
        try:
            manager = HUDManager(self.__arguments.huddb, self.__arguments.outdir)
            manager.getall()
            if self.__arguments.save:
                manager.save()
        except Exception:
            self.__logger.exception('An error occurred while working with the %s database file!',
                                    self.__arguments.huddb)

    def __init__(self) -> None:
        """
        Main constructor of the App class.
        """
        self.__setlogger()
        self.__parser_create()
        self.__parse_arguments()
