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
    url(r"^todo/$", views.todo, name="todo"),
    url(r"^copyright/$", views.copyright, name="copyright"),
    url(r"^loginredirect/$", views.loginredirect, name="loginredirect"),
]
