import uuid

class User: 
    def __init__ (self, email, password, id = None):
        self.email = email
        self.password = password
        self.id = id or str(uuid.uuid4())
    
