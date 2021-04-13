# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class HUDMessages:
    gh_errcode: str = 'GitHub API returned {:d} error code.'
    oth_errcode: str = 'Server returned {:d} error code.'
    db_notfound: str = 'Game database file not found: {}.'
    hud_updated: str = '{} has been updated. SHA512: {}, time: {}, filename: {}.'
    hud_uptodate: str = '{} is up to date.'
    hud_outdated: str = '{} is too outdated and no updates were found.'
    hud_error: str = 'Error while checking {} updates.'
