#!/usr/bin/env python3
# Time-stamp: <2024-09-10 07:16:00 rene>
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

import csv
import os


x = os.curdir
srcFile = os.path.join(x, "RESOURCES", "knowledge-links.csv")
dstFile = os.path.join(x, "tangodjsforgoodsound", "templates", "linkpage.html")
template1 = "<p class=\"linkpage\">" \
    "<a target=\"_blank\" href=\"%s\">%s</a><br>%s"
template2 = "<h2>%s</h2>"


if __name__ == "__main__":

    links = []
    with open(srcFile, "r") as csvfile:
        print(("%s found" % srcFile[2:]))
        xreader = csv.reader(csvfile)
        for row in xreader:
            if len(row) > 1:
                links.append(row)
    print(("%d lines read from %s" % (len(links), srcFile)))
    if links:
        content = []
        content.append("{% extends 'base.html' %}")
        content.append("{% block content %}")
        content.append("<h1>Knowledge</h1>")
        content.append("<div class=\"linkpage\">")
        for link, linkName, linkDesc in links:
            if linkName:
                if not linkDesc:
                    linkDesc = "-"
                content.append(template1 % (link, linkName, linkDesc))
            else:
                content.append(template2 % link)
        content.append("</div>")
        content.append("{% endblock %}")
        content.append('')
        with open(dstFile, "w") as f:
            f.write(os.linesep.join(content))
        print(("%d entries created" % (len(links))))
        print(("%s READY!" % dstFile[2:]))
    else:
        print(("%s not written" % dstFile[2:]))
