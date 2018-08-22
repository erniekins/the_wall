from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^welcome$', views.welcome),
	url(r'^validate$', views.validate),
	url(r'^message$', views.message),
	url(r'^comment/(?P<id>\d+)$', views.comment),
	url(r'^logout$', views.logout)
]