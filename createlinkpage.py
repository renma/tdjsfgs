#!/usr/bin/env python2
# Time-stamp: <2019-02-13 11:22:33 rene>
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


if __name__ == "__main__":

    template = (
        "{%% extends 'base.html' %%}\n"
        "{%% block content %%}\n"
        "{%% spaceless %%}\n"
        "<div class=\"linkpage\">\n"
         "    <h1>Links</h1>\n"
        "%s"
        "</div>\n"
        "{%% endspaceless %%}\n"
        "{%% endblock %%}\n")

    template2 = (
       "    <p class=\"1\"><a target=\"_blank\" href=\"%s\">%s</a></p>\n"
       "    <p class=\"2\">%s</p>")

    links = []
    x = os.curdir
    srcFile = os.path.join(x, "RESOURCES/linkpage.csv")
    dstFile = os.path.join(x, "tangodjsforgoodsound/templates/linkpage.html")
    
    with open(srcFile, "rb") as csvfile:
        print "%s found" % srcFile[2:]
        xreader = csv.reader(csvfile)
        for row in xreader:
            links.append(row)

    linksContent = ""
    if links:
        for link, linkName, linkDesc in links:
            if link:
                x = template2 % (link, linkName, linkDesc)
                linksContent = "%s%s\n" % (linksContent, x)
    content = template % linksContent

    with open(dstFile, "w") as f:
        f.write(content)
        print "%d link entries created" % (len(links))
        print "%s READY!" % dstFile[2:]
