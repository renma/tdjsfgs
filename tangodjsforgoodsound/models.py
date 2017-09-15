from __future__ import unicode_literals
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from choices import AUDIO_FORMAT_CHOICES, COMPUTER_CHOICES, GENDER_CHOICES, \
    MOSTLY_CHOICES, STYLE_CHOICES, YEAR_CHOICES, YESNO_CHOICES


@python_2_unicode_compatible
class DJ(models.Model):

    # Person Data
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,
                                blank=True)

    name = models.CharField(_("Name"),
                            max_length=200)

    gender = models.CharField(_("Gender"),
                              choices=GENDER_CHOICES,
                              max_length=50, default="MAL")

    country = CountryField(_("Country"),
                           null=True)

    since = models.IntegerField(_("Since"),
                                choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year)

    number_of_milongas = models.IntegerField(_("Number of milongas"),
                                             null=True)

    website = models.URLField(_("Website"),
                              max_length=200, null=True, blank=True)

    email = models.EmailField(_("Email"),
                              max_length=200, null=True)

    # Music Data
    style = models.CharField(_("Style"),
                             choices=STYLE_CHOICES,
                             max_length=80, null=True)

    cortinas = models.CharField(_("Tandas and cortinas"),
                                choices=YESNO_CHOICES,
                                max_length=80, null=True)

    audioformat = models.CharField(_("Main audio format"),
                                   choices=AUDIO_FORMAT_CHOICES,
                                   max_length=80, default="")

    audioformatmat2 = models.CharField(_("Alternative audio format"),
                                       choices=AUDIO_FORMAT_CHOICES,
                                       max_length=80, blank=True, default="")

    sources = models.CharField(_("Sources"),
                               max_length=200, null=True, blank=True)

    favorites = models.CharField(_("Personal favorites, decades"),
                                 max_length=200, null=True, blank=True)

    # Tech Data
    computer = models.CharField(_("Computer"),
                                choices=COMPUTER_CHOICES, default="",
                                max_length=80, null=True)

    computermodel = models.CharField(_("Computer model"),
                                     max_length=200, null=True, blank=True)

    player = models.CharField(_("Player"),
                              max_length=200, null=True)

    audiointerface = models.CharField(_("AudioInterface/DAC"),
                                      max_length=200, null=True)

    soundprocessor = models.CharField(_("Soundprocessor"),
                                      max_length=200, null=True, blank=True)

    other_equipment = models.CharField(_("Other equipment"),
                                       max_length=200, null=True, blank=True)

    compression = models.CharField(_("Compression"),
                                   choices=MOSTLY_CHOICES, default="NEV",
                                   max_length=80, null=True)

    equalization = models.CharField(_("Equalization"),
                                    choices=MOSTLY_CHOICES, default="NEV",
                                    max_length=80, null=True)

    music_remarks = models.CharField(_("Remarks"),
                                     max_length=200, null=True, blank=True)

    # Tech Data backup
    backup_computer = models.CharField(_("Computer"),
                                       choices=COMPUTER_CHOICES, default="",
                                       max_length=80, null=True)

    backup_computermodel = models.CharField(_("Computer model"),
                                            max_length=200, null=True)

    backup_player = models.CharField(_("Player"),
                                     max_length=200, null=True)

    backup_audiointerface = models.CharField(_("AudioInterface/DAC"),
                                             max_length=200,
                                             null=True, blank=True)

    backup_soundprocessor = models.CharField(_("Soundprocessor"),
                                             max_length=200, null=True,
                                             blank=True)

    backup_other_equipment = models.CharField(_("Other equipment"),
                                              max_length=200, null=True,
                                              blank=True)

    def __str__(self):
        return self.name
