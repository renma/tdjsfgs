#!/bin/bash
# Time-stamp: <2025-12-12 07:04:59 rene>
#
# Copyright (C) 2025 Rene Maurer
# This file is part of tangodjsforgoodsound.
#
# tangodjsforgoodsound is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# tangodjsforgoodsound is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------

WITH_RESTART=1

if [ ! "$(ps -x  | grep 63762 | grep -v grep)" ]; then
    if [ $WITH_RESTART -eq 1 ]; then
        echo "Server down (=> restart triggered)"
        /home/tdjsfgs/ALL/mysite/tdjs start prod >> /home/tdjsfgs/ALL/mysite/log.txt 2>&1
    else
        echo "Server down"
    fi
fi
