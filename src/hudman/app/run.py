# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import sys

from hudman.app import App


def setup_log() -> None:
    """
    Setup root logger of the application.
    """
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    e_handler = logging.StreamHandler(sys.stdout)
    e_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
    root.addHandler(e_handler)


def main() -> None:
    """
    The main entry point of the application.
    """
    try:
        setup_log()
        App().run()
    except Exception as ex:
        print(f'An error occurred while running application: {ex}')


if __name__ == '__main__':
    main()
