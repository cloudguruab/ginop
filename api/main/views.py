from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
import logging, time, json, os, datetime
from ..dev.blockchain import chain
from ..dev.common.exceptions import FailedChainEventExeception
from .schema import UserSerializer

# logger = logging.getLogger(__name__) NOTE: config logger
blockchain = chain.Blockchain()

class UserView(viewsets.ModelViewSet):
    #NOTE: make this your clock in and out endpoints 
    """
    Endpoint that allows users to be viewed or edisted
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


    

# @bp.route('/chain', methods=['GET'])
# def private_chain():
#     chain_data = []
#     for block in blockchain.chain:
#         chain_data.append(block.__dict__)
#     return json.dumps({"length": len(chain_data),
#                        "chain": chain_data})
