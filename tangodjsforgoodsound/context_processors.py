# Time-stamp: <2017-11-18 17:12:41 rene>
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

import datetime
from version import VERSION, TIMESTAMP


def appData(request):
    version = VERSION
    lastupdate = TIMESTAMP.split("<")[1].split()[0]
    y, m, d = lastupdate.split("-")
    return {"APP_VERSION": version,
            "APP_DATE": lastupdate,
            "APP_YEAR": y,
            "CURRENT_YEAR": datetime.datetime.now().year}
