
class AuthService:
    def __init__(self, user_repo, token_repo, password_hasher, jwt_service):
        self.user_repo = user_repo
        self.token_repo = token_repo
        self.password_hasher = password_hasher
        self.jwt_service = jwt_service

    def register(self, email: str, password: str):
        if not email or not password:
            raise ValueError("Invalid data")

        if self.user_repo.find_by_email(email):
            raise ValueError("User already exists")

        hashed = self.password_hasher.hash(password)
        user = self.user_repo.create(email, hashed)

        return user

    def login(self, email: str, password: str):
        user = self.user_repo.find_by_email(email)

        if not user:
            raise ValueError("User not found")
        
        if not self.password_hasher.verify(password, user.password):
            raise ValueError("Incorrect password")

        token, expires_in = self.jwt_service.generate(user.id)

        self.token_repo.store(token, user.id, expires_in)

        return {"access_token": token, "expires_in":expires_in}