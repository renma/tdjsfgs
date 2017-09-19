import datetime
from django.utils.translation import ugettext as _


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
    ("WAV", _("WAV Resource Interchange File Format (.wav)")),
    ("ADA", _("ADA Advanced Digital Audio (.ada)")),
    ("ALAC", _("ALAC Apple Lossless Audio Codec (.m4a, .mp4)")),
    ("APE", _("APE Monkey's Audio (.ape, .mac)")),
    ("FLAC", _("FLAC Free Lossless Audio Codec (.flac, .fla)")),
    ("SHN", _("SHN Shorten (.shn)")),
    ("TTA", _("TTA The True Audio (.tta)")),
    # ("WMA", _("WMA Windows Media Audio LOSSLESS (.wma)")),
    ("WV",  _("WV WavPack LOSSLESS (.wv)")),
)


COMPUTER_CHOICES = (
    ("PCW", _("PC Windows")),
    ("PCL", _("PC Linux")),
    ("MAC", _("MAC")),
    ("MOB", _("Mobile device (Tablet, Smartphone, iPhone, iPad, ...)")),
)


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))
YEAR_CHOICES.reverse()
