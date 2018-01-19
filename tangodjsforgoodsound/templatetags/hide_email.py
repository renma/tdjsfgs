# Time-stamp: <2018-01-19 15:18:30 rene>
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

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def encode_mailto(text):
    """gugus msut be present in the html header."""
    if "@" not in text:
        return text
    a, b = text.split("@")
    script = "<script type=\"text/javascript\">gugus('%s', '%s', '');</script>"
    return mark_safe(script % (a, b))
