# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from hudman.app import App


def main():
    """
    The main entry point of the application.
    """
    try:
        App().run()
    except Exception as ex:
        print(f'An error occurred while running application: {ex}')


if __name__ == '__main__':
    main()
