# coding=utf-8

# This file is a part of HUD mirror script. For more information
# visit official site: https://www.easycoding.org/projects/hudman
#
# Copyright (c) 2016 - 2019 EasyCoding Team.
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


class HUDSettings:
    ua_curl: str = 'Curl'
    ua_wget: str = 'Wget'
    log_stdfmt = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'


class HUDMessages:
    gh_errcode: str = 'GitHub API returned {:d} error code.'
    oth_errcode: str = 'Server returned {:d} error code.'
    db_notfound: str = 'Game database file not found: {}.'
    hud_updated: str = '{} has been updated. SHA512: {}, time: {}, filename: {}.'
    hud_uptodate: str = '{} is up to date.'
    hud_outdated: str = '{} is too outdated and no updates were found.'
    hud_error: str = 'Error while checking {} updates.'
