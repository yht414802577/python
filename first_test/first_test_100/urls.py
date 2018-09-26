# encoding: utf-8
"""
@version:??
@author:df
"""

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^table/', views.table),
    url(r'^dashboard/', views.dashboard),
    url(r'^icons/', views.icons),
    url(r'^maps/', views.maps),
    url(r'^notifications/', views.notifications),
    url(r'^template/', views.template),
    url(r'^typography/', views.typography),
    url(r'^upgrade/', views.upgrade),
    url(r'^user/', views.user),
]
