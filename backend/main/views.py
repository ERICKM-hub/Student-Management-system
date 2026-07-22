from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from rest_framework.response import Response
from .serializers import userProfileSerializers 
from .models import UserProfile

@login_required
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated]) 
def Users_view(request):
    if request.method == "GET":
        queryset = UserProfile.objects.all()
        serializer = userProfileSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = userProfileSerializers(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
