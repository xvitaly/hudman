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

from setuptools import setup, find_packages

setup(
    name='hudman',
    version='2.1.0',
    packages=find_packages(),
    url='https://github.com/xvitaly/hudman',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'hudman = hudman.app.run:main',
        ],
    },
    install_requires=['requests'],
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    description='Simple script to create a local HUD mirror'
)
