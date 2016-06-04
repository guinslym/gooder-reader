from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import GRUser

#http GET http://localhost:8004/user/ pk=1
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user(request, **kwargs):
    pk = request.data['pk']

    user = GRUser.objects.get(pk=pk)
    serializer = GRUserSerializer(user)
    return Response(serializer.data)
