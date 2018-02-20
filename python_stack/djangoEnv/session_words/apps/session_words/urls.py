from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^enter_info$', views.enter_info),
    url(r'^clear$', views.clear),
]
