#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Time-stamp: <2020-11-11 08:07:36 rene>
#
# Copyright (C) 2020 Rene Maurer
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

import logging
import os
import sys
from rpystart import BaseOptionParser


__version__ = 1
logger = logging.getLogger()


def main():
    usage = list()
    usage.append("%prog destinationfile cssfilename")
    usage.append("")
    usage.append("Replace css in destinationfile")

    parser = BaseOptionParser(usage, __version__, configBaseLogging=True,
                              consoleDefaultLogLevel="info")

    (options, args) = parser.parse_args()
    if not len(args) == 2:
        parser.errormessage("Wrong parameters")
        return -1
    filename = args[0]
    css = args[1]
    if not os.path.isfile(filename):
        parser.errormessage("%s is not a file" % filename)
        return -1

    content = open(filename, "r").read()
    s0 = "static '"
    s1 = s0 + "style_"
    index1 = content.find(s1)
    s2 = "' "
    index2 = content[index1:].find(s2)
    oldcss = content[index1 + len(s0):index1 + index2].strip()
    logger.info("%s => %s" % (oldcss, css))
    content = content.replace(oldcss, css)
    open(filename, "w").write(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
