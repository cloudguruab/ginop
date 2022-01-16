from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ChainEventsModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ChainEventsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ChainEventsModel
        fields = ['index', 'previous_hash', 'curr_hash']
    

#add your own custom serializers for new schema models below.