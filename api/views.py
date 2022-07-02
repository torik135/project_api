from rest_framework.response import Response
from rest_framework.decorators import api_view

from app_portofolio.models import ProjectList, TechChoices
from .serializers import ProjectListSerializers, TechChoicesSerializers

@api_view(['GET'])
def getProject(req):
  project_query = ProjectList.objects.all()
  project_serializers = ProjectListSerializers(project_query, many=True)
  return Response(project_serializers.data)

@api_view(['GET'])
def getProjectBySlug(req, slug):
  project_slug_query = ProjectList.objects.get(slug=slug)
  project_slug_serializers = ProjectListSerializers(project_slug_query, many=False)
  return Response(project_slug_serializers.data)


# Query err <----ERROR
# @api_view(['GET'])
# def getProjectById(req, id):
#   project_id_query = ProjectList.objects.filter(pk=id).get()
#   project_id_serializers = ProjectListSerializers(project_id_query, many=False)
#   return Response(project_id_serializers.data)

@api_view(['GET'])
def getTech(req):
  tech_query = TechChoices.objects.all()
  tech_serializers = TechChoicesSerializers(tech_query, many=True)
  return Response(tech_serializers.data)

# def getTechBySlug(req, project_id):

