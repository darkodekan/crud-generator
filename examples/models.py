from sqla_wrapper import SQLAlchemy

db = SQLAlchemy()

class product(db.Model):
    __tablename__ = "product"
    
    
        
    id = db.Column(db.Integer, primary_key=True)

        
    
    
    
    name = db.Column(db.String)


    
    

class order(db.Model):
    __tablename__ = "order"
    
    
        
    id = db.Column(db.Integer, primary_key=True)

        
    
    
    
    date = db.Column(db.String)


    
    

db.create_all()