from django.urls import path
from .views import (
  getProject, 
  getProjectBySlug, 

  getTech,
  getTechBySlug,
  )

urlpatterns = [
  # PROJECTS
  path('projects/all/', getProject),
  path('projects/<slug:slug>/', getProjectBySlug),
  # path('projects/<int:id>/', getProjectById),
  # TECH
  path('tech/all/', getTech),
  path('tech/<slug:tech_slug>/', getTechBySlug),
]
