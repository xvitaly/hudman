# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

__all__ = ['ArchiveNotValid', 'DBFileNotFound']


class ArchiveNotValid(Exception):
    """
    Base class for the archive validation errors.
    """


class DBFileNotFound(FileNotFoundError):
    """
    Base class for the database file not found errors.
    """
