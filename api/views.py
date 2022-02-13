
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated


from .serializers import ProjectSerializer, ProfileSerializer

from projects.models import Project
from users.models import Profile

# Create your views here.
@api_view(['GET'])
def gettest(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
        ]

    return Response(routes)

@api_view(['GET'])
def getprojects(request):
    projects= Project.objects.all()
    serializer= ProjectSerializer(projects, many= True)

    return Response(serializer.data)

@api_view(['GET' , 'POST'])
def getproject(request,pk):
    project= Project.objects.get(id=pk)
    serializer= ProjectSerializer(project, many= False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createproject(request):
    user= request.user.profile

    data= request.data

    print(data)

    projects= Project.objects.all()
    serializer= ProjectSerializer(projects, many= True)

    return Response(serializer.data)


@api_view(['GET'])
def getprofiles(request):
    profiles= Profile.objects.all()
    serializer= ProfileSerializer(profiles, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def getprofile(request, pk):
    profiles= Profile.objects.get(id=pk)
    serializer= ProfileSerializer(profiles, many= False)

    return Response(serializer.data)


# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Profile.objects.all().order_by('-created')
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]

