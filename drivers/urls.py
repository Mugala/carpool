from django.conf.urls import url
from . import views

urlpatterns = [
    url('^drivers/', views.welcome, name = "dwelcome"),
]