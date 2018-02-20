from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(\d+)$', views.show),
    url(r'^(\w+)/edit$', views.edit),
    url(r'^(\w+)/delete$', views.delete),
]
