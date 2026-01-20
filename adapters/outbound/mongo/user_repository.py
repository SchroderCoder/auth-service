from domain.ports.user_repository import UserRepository

class MongoUserRepository(UserRepository):
    def __init__(self, collection):
        self.collection = collection

    def find_by_email(self, email):
        return self.collection.find_one({"email": email})

    def create(self, email, password):
        res = self.collection.insert_one({
            "email": email,
            "password": password
        })
        return {"id": str(res.inserted_id), "email": email}
