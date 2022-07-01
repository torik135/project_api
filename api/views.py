from rest_framework.response import Response
from rest_framework.decorators import api_view

from app_portofolio.models import ProjectList
from .serializers import ProjectListSerializers

@api_view(['GET'])
def getProject(req):
  project_query = ProjectList.objects.all()
  project_serializers = ProjectListSerializers(project_query, many=True)
  return Response(project_serializers.data)

