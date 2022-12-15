# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class Messages:
    """
    Class for working with project message strings.
    """

    db_notfound: str = 'Game database file not found: {}.'
    hud_downloaded: str = '{} was downloaded. SHA512: {}, time: {}, filename: {}.'
    hud_hash_missmatch: str = '{} download failed due to hash missmatch.'
    hud_updated: str = '{} has been updated. SHA512: {}, time: {}, filename: {}.'
    hud_uptodate: str = '{} is up to date.'
    hud_outdated: str = '{} is too outdated and no updates were found.'
    hud_error: str = 'An error while checking for {} updates. The inner exception was: "{}".'
    hud_exception: str = 'An error while checking for {} updates.'
