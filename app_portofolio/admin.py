from django.contrib import admin
from .models import TechChoices, ProjectList

class ProjectListAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Project Detail', {'fields': ['project_name', 'author', 'project_desc']}),
    ('Project Link', {'fields': ['code', 'web_link']}),
    ('Project Tech', {'fields': ['tech', 'project_type']}),
  ]

  list_display = (
    'project_name',
    'author',
    'project_type',
  )

  search_fields = ['project_name', 'project_desc']
  list_filter = ['project_type', 'author']

class TechChoicesAdmin(admin.ModelAdmin):
  list_display = (
    'tech_name',
    'tech_desc',
  )

  search_fields = ['tech_name']

admin.site.register(ProjectList, ProjectListAdmin)
admin.site.register(TechChoices, TechChoicesAdmin)
