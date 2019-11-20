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

"""Module for time tracking"""

import logging
import threading
import time

logger = logging.getLogger(__name__)

_log_level = logging.INFO
_start_times = {}
_timer_lock = threading.RLock()


def set_log_level(new_level: int):
    global _log_level
    if isinstance(new_level, int):
        with _timer_lock:
            _log_level = new_level
    else:
        raise TypeError(f"Expected int, got {type(new_level)} - hint: use built-ins, such as logging.INFO")


def start(name: str):
    """
    Record a start time for a given name. If it already exists, the time difference is logged and the new time is set.
    :param name: str identifier to use for tracking and logging this timer
    :return: None
    """
    current_time = time.time()
    with _timer_lock:
        existing_start_time = _start_times.get(name)
        if existing_start_time:
            _log_time(name, current_time - existing_start_time)
        _start_times[name] = current_time
        logger.debug(f"Start time recorded for '{name}'")


def stop(name: str):
    """
    Log the time difference between the recorded start time for given name and now.
    :param name: str identifier that was used with start() call
    :raises: ValueError when no start time is found for the provided name
    :return: None
    """
    current_time = time.time()
    with _timer_lock:
        start_time = _start_times.pop(name, None)
        if start_time is None:
            msg = f"No time record for '{name}'"
            logger.error(msg)
            raise ValueError(msg)
        else:
            _log_time(name, current_time - start_time)


def _log_time(name: str, time_difference: float):
    logger.log(_log_level, f"'{name}' completed in {time_difference} seconds")
