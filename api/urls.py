from django.urls import path
from .views import getProject

urlpatterns = [
  path('v1/list/', getProject),
]
