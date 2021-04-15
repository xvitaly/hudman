# coding=utf-8

# SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os


class Settings:
    """
    Class for working with project settings.
    """

    apifetch_user_agent: str = 'Curl'
    """
    Return HTTP_USER_AGENT field used for the external API requests.
    """

    download_user_agent: str = 'Wget'
    """
    Return HTTP_USER_AGENT field used for the file downloads.
    """

    logger_format: str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    """
    Return logger format string.
    """

    github_user: str = os.getenv('HUDMAN_LOGIN')
    """
    Return GitHub API user name.
    """

    github_token: str = os.getenv('HUDMAN_APIKEY')
    """
    Return GitHub API access token.
    """
