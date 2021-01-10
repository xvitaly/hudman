# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse

from hudman import HUDMirror


def main():
    # Parse command-line arguments...
    parser = argparse.ArgumentParser()
    parser.add_argument('--huddb', '-d', help='Specify path to HUDs database file.', required=True)
    parser.add_argument('--outdir', '-o', help='Specify path to save downloaded files.', required=True)
    parser.add_argument('--save', '-s', help='Automatically save changes in HUD database file.', action='store_true', required=False)
    cmdline = parser.parse_args()

    # Run mirror script...
    hm = HUDMirror(cmdline.huddb, cmdline.outdir)
    hm.getall()

    # Saving changes if enabled...
    if cmdline.save:
        hm.save()


if __name__ == '__main__':
    main()
