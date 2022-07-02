from django.contrib import admin
from .models import TechChoices, ProjectList

@admin.register(ProjectList)
class ProjectListAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Project Detail', {'fields': ['project_name', 'slug', 'author', 'project_desc']}),
    ('Project Link', {'fields': ['code', 'web_link', 'project_img']}),
    ('Project Tech', {'fields': ['tech', 'project_type']}),
  ]

  list_display = (
    'project_name',
    'author',
    'project_type',
  )

  prepopulated_fields = {'slug': ('project_name', )}

  search_fields = ['project_name', 'project_desc']
  list_filter = ['project_type', 'author']

@admin.register(TechChoices)
class TechChoicesAdmin(admin.ModelAdmin):
  list_display = (
    'tech_name',
    'tech_desc',
  )

  prepopulated_fields = {'tech_slug': ('tech_name', )}
  search_fields = ['tech_name']
