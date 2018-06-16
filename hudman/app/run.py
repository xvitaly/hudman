#!/usr/bin/python3
# coding=utf-8

#
# This file is a part of HUD mirror script. For more information
# visit official site: https://www.easycoding.org/projects/hudman
#
# Copyright (c) 2016 - 2018 EasyCoding Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from argparse import ArgumentParser
from hudman import HUDMirror


def main():
    # Parse command-line arguments...
    parser = ArgumentParser()
    parser.add_argument('--gamedb', '-d', help='Specify path to game database file.', required=True)
    parser.add_argument('--outdir', '-o', help='Specify path to save downloaded files.', required=True)
    cmdline = parser.parse_args()

    # Run mirror script...
    HUDMirror(cmdline.gamedb, cmdline.outdir)


if __name__ == '__main__':
    main()
