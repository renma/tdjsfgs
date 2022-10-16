# Time-stamp: <2022-10-13 08:08:20 rene>
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
from .version import __version__, __date__


def appData(request):
    version = __version__
    lastupdate = __date__.split(" ")[0]
    y, m, d = lastupdate.split("-")
    return {"APP_VERSION": version,
            "APP_DATE": lastupdate,
            "APP_YEAR": y,
            "CURRENT_YEAR": datetime.datetime.now().year}
