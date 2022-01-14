from .. import db

class Ginop(db.Model):
    
    __tablename__ = 'ginop'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
        
    def __repr__(self):
        return f'<Ginop {self.username}'
    
class ChainEventsModel(db.Model):
    # created_at = db.Column(db.DateTime, nullable=False)
    # signed_at = db.Column(db.DateTime, nullable=False)
    # signature_key = db.Column(db.String(255), nullable=False)
    # workflow_type = db.Column(db.String(255), nullable=False)
    # geospacial = bool  
    # sms = bool 
    # biometric = bool
    pass
    