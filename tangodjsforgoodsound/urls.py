from django.conf.urls import url
# from django.views.generic.base import RedirectView
from . import views


# favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [

    url(r'^$', views.index, name="index"),

    # example: /5/
    url(r"^(?P<dj_id>[0-9]+)/$", views.djdetail, name="djdetail"),
    url(r"^contact/$", views.contact, name="contact"),
    url(r"^contactfeedback/$", views.contactfeedback, name="contactfeedback"),
    url(r"^djedit/$", views.djedit, name="djedit"),
    url(r"^about/$", views.about, name="about"),
    url(r"^todo/$", views.todo, name="todo"),
#    url(r'^favicon\.ico$', favicon_view),
]
