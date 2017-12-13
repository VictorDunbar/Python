from django.conf.urls import url
from . import views

urlpatterns = [
    url('^generate$', views.generate),
    url('^reset$', views.reset),
    url('^$', views.index),
    # url('^RWG_app$', views.index)
]