from django.urls import path
from .views import getProject, getTech, getProjectBySlug

urlpatterns = [
  # PROJECTS
  path('projects/all/', getProject),
  path('projects/<slug:slug>/', getProjectBySlug),
  # path('projects/<int:id>/', getProjectById),
  # TECH
  path('tech/all/', getTech),
  # path('tech/<str:slug>/', getTechBySlug),
]
