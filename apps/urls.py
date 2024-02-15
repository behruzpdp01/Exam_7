from django.conf import urls
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path, include

from apps.views import PeopleListView,PersonDeleteView,PersonUpdateView

urlpatterns = [
    path('',PeopleListView.as_view(),name='list_people'),
    path('delete/<int:pk>',PersonDeleteView.as_view(),name='delete_person'),
    path('update-user/<int:pk>', PersonUpdateView.as_view(), name='update_person'),
]