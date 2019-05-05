from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import HelloSerializer
# Create your views here.

class HelloApiView(APIView):
    """Tes API View"""
    serializer_class = HelloSerializer
    def get(self, request,format=None):
        """returns a list of APIView feature"""


        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'It is similar to a traditional django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """handles updating an object."""
        return Response({'message':'put'})

    def patch(self, request, pk=None):
        """patch request, only updates fields provided in the request."""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Returns a hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})