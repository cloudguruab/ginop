from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
import logging, time, json, os, datetime
from ..dev.blockchain import chain
from ..dev.common.exceptions import FailedChainEventExeception
from .schema import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


blockchain = chain.Blockchain()


class UserView(viewsets.ModelViewSet):
    """
    Endpoint that allows users to be viewed or edisted
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PrivateChainView(APIView):
    """
    Example endpoint for handling actions on the private chain.
    """
        
    def get(self, request, format=None, *args, **kwargs):
        chain_data = []
        
        for block in blockchain.chain:
            chain_data.append(block.__dict__)
        
        context = json.dumps({"length": len(chain_data),
                        "chain": chain_data})
        
        return Response(context, status=status.HTTP_200_OK)


#write your own custom endpoints below.
