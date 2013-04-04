# coding: utf-8

# archversion - Archlinux Version Controller
# Copyright © 2012 Sébastien Luttringer
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

'''Archlinux Version Controller Package'''

import logging

# Init log systems
logging.basicConfig(format="%(levelname)s: %(message)s")

# Annouced version
VERSION = "0"

# Stored list of packagas we want to track
DEFAULT_CONFIG_FILENAME = "archversion.conf"

# Cache is stored package versions
DEFAULT_CACHE_FILENAME = "archversion.cache"

# user agent using with http request
USER_AGENT = "archversion v%s" % VERSION
