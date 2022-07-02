from rest_framework.response import Response
from rest_framework.decorators import api_view

from app_portofolio.models import ProjectList, TechChoices
from .serializers import ProjectListSerializers, TechChoicesSerializers

@api_view(['GET'])
def getProject(request):
  project_query = ProjectList.objects.all()
  project_serializers = ProjectListSerializers(project_query, many=True)
  return Response(project_serializers.data)

@api_view(['GET'])
def getProjectBySlug(request, slug):
  project_slug_query = ProjectList.objects.get(slug=slug)
  project_slug_serializers = ProjectListSerializers(project_slug_query, many=False)
  return Response(project_slug_serializers.data)

@api_view(['GET'])
def getProjectByProjectType(request, project_type):
  project_pt_query = ProjectList.objects.filter(project_type=project_type)
  project_pt_serializers = ProjectListSerializers(project_pt_query, many=True)
  return Response(project_pt_serializers.data)

@api_view(['GET'])
def getTech(request):
  tech_query = TechChoices.objects.all()
  tech_serializers = TechChoicesSerializers(tech_query, many=True)
  return Response(tech_serializers.data)

@api_view(['GET'])
def getTechBySlug(request, tech_slug):
  tech_slug_query = TechChoices.objects.get(tech_slug=tech_slug)
  tech_slug_serializers = TechChoicesSerializers(tech_slug_query, many=False)
  return Response(tech_slug_serializers.data)

