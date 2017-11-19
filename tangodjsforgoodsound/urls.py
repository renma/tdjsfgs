# Time-stamp: <2017-11-18 18:12:26 rene>
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

from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index, name="index"),

    # example: /5/
    url(r"^(?P<dj_id>[0-9]+)/$", views.djdetail, name="djdetail"),
    url(r"^contact/$", views.contact, name="contact"),
    url(r"^contactfeedback/$", views.contactfeedback, name="contactfeedback"),
    url(r"^djedit/$", views.djedit, name="djedit"),
    url(r"^about/$", views.about, name="about"),
    url(r"^more/$", views.more, name="more"),
    url(r"^copyright/$", views.copyright, name="copyright"),
    url(r"^loginredirect/$", views.loginredirect, name="loginredirect"),
    url(r"^customlogout/$", views.customlogout, name="customlogout"),
]
