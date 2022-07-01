from rest_framework import serializers
from app_portofolio.models import ProjectList

class ProjectListSerializers(serializers.ModelSerializer):
  class Meta:
    model = ProjectList
    fields = '__all__'
