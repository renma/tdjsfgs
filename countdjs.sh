#!/bin/bash
# Time-stamp: <2025-10-15 08:17:17 rene>
#
# Copyright (C) 2017 Rene Maurer
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

DB=db.sqlite3

echo "Count all DJs in $DB"
sqlite3 $DB <<'END_SQL'
SELECT COUNT(*) FROM tangodjsforgoodsound_dj;
END_SQL
echo "Count DJs with 'milongas > 0' in $DB"
sqlite3 $DB <<'END_SQL'
SELECT COUNT(*) FROM tangodjsforgoodsound_dj WHERE number_of_milongas > 0;
END_SQL
