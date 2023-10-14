# Time-stamp: <2023-10-10 11:23:26 rene>
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
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = (
    ("MAL", _("Male")),
    ("FEM", _("Female")),
)


STYLE_CHOICES = (
    ("TRA", _("Traditional")),
    ("ALT", _("Alternative")),
    ("TA", _("Traditional and alternative")),
)


YESNO_CHOICES = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)


MOSTLY_CHOICES = (
    ("NEV", _("Never")),
    ("SOM", _("Sometimes")),
    ("MOS", _("Mostly")),
    ("ALW", _("Always")),
)


AUDIO_FORMAT_CHOICES = (
    ("AIFF", _("AIFF Audio Interchange File Format (.aiff, aif)")),
    ("FLAC", _("FLAC Free Lossless Audio Codec (.flac, .fla)")),
    ("WAV", _("WAV Resource Interchange File Format (.wav)")),
    ("ADA", _("ADA Advanced Digital Audio (.ada)")),
    ("ALAC", _("ALAC Apple Lossless Audio Codec (.m4a, .mp4)")),
    ("APE", _("APE Monkey's Audio (.ape, .mac)")),
    ("SHN", _("SHN Shorten (.shn)")),
    ("TTA", _("TTA The True Audio (.tta)")),
    ("WV", _("WV WavPack LOSSLESS (.wv)")),
    ("ANALOG", _("ANALOG Playback of LPs/Shellacs")),
)


COMPUTER_CHOICES = (
    ("PCW", _("PC Windows")),
    ("PCL", _("PC Linux")),
    ("MAC", _("MAC")),
    ("MOB", _("Mobile device (Tablet, Smartphone, iPhone, iPad, ...)")),
    ("TTA", _("Turntable(s)")),  # Yes, we already know that this is not a computer ;-)
)


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))
YEAR_CHOICES.reverse()


NUM_MILONGA_CHOICES = [(0, 0)]
for i in range(30):
    r = (i + 1) * 10
    NUM_MILONGA_CHOICES.append((r, r))
for i in range(14):
    r = 300 + ((i + 1) * 50)
    NUM_MILONGA_CHOICES.append((r, r))
for i in range(5):
    r = 1000 + ((i + 1) * 200)
    NUM_MILONGA_CHOICES.append((r, r))
