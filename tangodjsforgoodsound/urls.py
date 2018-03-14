# Time-stamp: <2018-03-13 07:22:49 rene>
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
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from . import views, forms


urlpatterns = [

    url(r'^$', views.index, name="index"),

    # example: /5/
    url(r"^(?P<dj_id>[0-9]+)/$", views.djdetail, name="djdetail"),
    url(r"^contact/$", views.contact, name="contact"),
    url(r"^contactfeedback/$", views.contactfeedback, name="contactfeedback"),
    url(r"^djedit/$", views.djedit, name="djedit"),
    url(r"^mission/$", views.mission, name="mission"),
    url(r"^more/$", views.more, name="more"),
    url(r"^copyright/$", views.copyright, name="copyright"),
    url(r"^linkpage/$", views.linkpage, name="linkpage"),
    url(r"^loginredirect/$", views.loginredirect, name="loginredirect"),
    url(r"^customlogout/$", views.customlogout, name="customlogout"),

    url("^accounts/password_reset/$", auth_views.password_reset,
        {"password_reset_form": forms.EmailValidationOnForgotPassword},
        name="password_reset"),

    url(r"^djedit/password/$", views.change_password,
        name="change_password"),

    url(r"^login/$", auth_views.login, name="login"),
    url(r"^djdelete/$", views.djdelete, name="djdelete"),
    url(r"^djdeleted/$", views.djdeleted, name="djdeleted"),

    url(r"^register/$", views.register, name="register"),
    url(r"^registered/$", views.registered, name="registered"),

    # Support old urls (google-search)
    url(r"^about/$", RedirectView.as_view(url="/mission")),

]
