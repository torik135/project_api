from rest_framework import serializers
from app_portofolio.models import ProjectList

class ProjectListSerializers(serializers.ModelSerializer):
  project_type = serializers.SerializerMethodField()
  class Meta:
    model = ProjectList
    fields = '__all__'

  def get_project_type(self, obj):
    print("THIS ------>", obj.project_type)
    if obj.project_type == 'FE':
      return 'Front End'
    elif obj.project_type == 'BE':
      return 'Back End'
    elif obj.project_type == 'FS':
      return 'Full Stack'
    elif obj.project_type == 'PL':
      return 'Plain / Native'
    else: return 'NULL'
