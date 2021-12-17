from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GinopDB(db.Model):
    
    __tablename__ = 'ginop'
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    signed_at = db.Column(db.DateTime, nullable=False)
    signature_key = db.Column(db.String(255), nullable=False)
    workflow_type = db.Column(db.String(255), nullable=False)
    # geospacial = bool  
    # sms = bool 
    # biometric = bool
    
    def __repr__(self):
        return f'<GinopDB {self.signature_key}'