# encoding: utf-8
"""
@version:??
@author:df
"""

from django.conf.urls import  url
import views

urlpatterns = [
    url(r'^^$', views.index),
]
