from domain.ports.user_repository import UserRepository
from domain.entities.user import User

class MongoUserRepository(UserRepository):
    def __init__(self, collection):
        self.collection = collection

    def find_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if not user:
            return None
        
        return User(user["email"], user["password"], str(user["_id"]))
    
    def create(self, email, password):
        res = self.collection.insert_one({
            "email": email,
            "password": password
        })

        return User(email, password, str(res.inserted_id) )

