from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    
    def __repr__(self):
        return f'<GinopDB {self.username} >'

class ChainEventsModel(models.Model):
    index = models.IntegerField()
    previous_hash = models.CharField(max_length=255)
    curr_hash = models.CharField(max_length=255)
    
    def __repr__(self):
        return f'<ChainEventsModel {self.index}>'

#write your own custom models below if needed.