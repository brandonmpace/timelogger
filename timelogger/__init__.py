# -*- coding: UTF-8 -*-
# Copyright (C) 2019 Brandon M. Pace
#
# This file is part of timelogger
#
# timelogger is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# timelogger is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with timelogger.
# If not, see <https://www.gnu.org/licenses/>.

"""Package for logging time differences between different points of Python programs"""

__author__ = "Brandon M. Pace"
__copyright__ = "Copyright 2019, Brandon M. Pace"
__license__ = "GNU LGPL 3+"
__maintainer__ = "Brandon M. Pace"
__status__ = "Development"
__version__ = "0.0.2"

import logging

from .timer import set_log_level, start, stop

logger = logging.getLogger(__name__)
