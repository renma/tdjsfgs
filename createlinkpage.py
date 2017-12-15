#!/usr/bin/env python2
# Time-stamp: <2017-12-15 22:28:37 rene>
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
srcFile = os.path.join(x, "RESOURCES", "linkpage.csv")
dstFile = os.path.join(x, "tangodjsforgoodsound", "templates", "linkpage.html")
template = "<p class=\"linkpage\">" \
    "<a target=\"_blank\" href=\"%s\">%s</a><br />%s"


if __name__ == "__main__":

    links = []
    with open(srcFile, "rb") as csvfile:
        xreader = csv.reader(csvfile)
        for row in xreader:
            links.append(row)

    if links:
        content = []
        content.append("{% extends 'base.html' %}")
        content.append("{% block content %}")
        content.append("<h1>Links</h1>")
        content.append("<div class=\"linkpage\">")
        for link, linkName, linkDesc in links:
            if link:
                content.append(template % (link, linkName, linkDesc))
        content.append("</div>")
        content.append("{% endblock %}")
        with open(dstFile, "w") as f:
            f.write(os.linesep.join(content))
        print "%d links written to %s" % (len(links), dstFile)
    else:
        print "%s not written" % dstFile
