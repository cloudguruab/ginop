from django.contrib.auth.models import User
from .models import ChainEventsModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ChainEventsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ChainEventsModel
        pass
    
    pass #TODO: