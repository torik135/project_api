from django.urls import path
from .views import getProject, getTech

urlpatterns = [
  path('projects/all/', getProject),
  path('tech/all/', getTech),
]
