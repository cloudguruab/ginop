from django.db import models

class User(models.Model):
    username = None
    email = None
    special_character = None
    
    def __repr__(self):
        return f'<GinopDB {self.username} >'

class ChainEventsModel(models.Model):
    # created_at = db.Column(db.DateTime, nullable=False)
    # signed_at = db.Column(db.DateTime, nullable=False)
    # signature_key = db.Column(db.String(255), nullable=False)
    # workflow_type = db.Column(db.String(255), nullable=False)
    # geospacial = bool  
    # sms = bool 
    # biometric = bool
    pass

#write your own custom models below if needed.