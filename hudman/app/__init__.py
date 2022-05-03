# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import logging

from hudman import HUDManager


class App:
    """
    Class with command-line tool implementation.
    """

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
        self.__parser_add_groups()
        self.__parser_add_arguments()

    def __parser_add_groups(self) -> None:
        """
        Add a new mutally excludive group to the command-line arguments parser.
        """
        action = self.__parser.add_mutually_exclusive_group(required=True)
        action.add_argument('--download', '-d', help='Download all HUDs without updating them.', action='store_true')
        action.add_argument('--update', '-u', help='Update all HUDs and download only new files.', action='store_true')

    def __parser_add_arguments(self) -> None:
        """
        Add new options to the command-line arguments parser.
        """
        self.__parser.add_argument('--huddb', '-a', help='Path to the local HUDs database file.', required=True)
        self.__parser.add_argument('--outdir', '-o', help='Path to the output directory for storing downloaded files.',
                                   required=True)

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
            if self.__arguments.download:
                manager.getall()
            else:
                manager.updateall()
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
