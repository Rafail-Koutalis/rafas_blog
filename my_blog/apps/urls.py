
from django.contrib import admin
from django.urls import path
from .views import AppsViews

urlpatterns = [
    path('',AppsViews.all_apps,name='apps'),
    path('payments/',AppsViews.payments,name='payments'),
    path('study/',AppsViews.study,name='study'),
    path('e_wallet/',AppsViews.e_wallet,name='e_wallet'),
    path('bio/',AppsViews.bio,name='bio'),
]
   