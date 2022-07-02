from django.urls import path
from .views import (
  getProject, 
  getProjectBySlug,
  getProjectByProjectType,
  getTech,
  getTechBySlug,
  )

urlpatterns = [
  # PROJECTS
  path('projects/all/', getProject),
  path('projects/<slug:slug>/', getProjectBySlug),
  path('projects/type/<str:project_type>/', getProjectByProjectType),
  # TECH
  path('tech/all/', getTech),
  path('tech/<slug:tech_slug>/', getTechBySlug),
]
