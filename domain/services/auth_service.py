class AuthService:
    def __init__(self, user_repo, token_repo, password_hasher):
        self.user_repo = user_repo
        self.token_repo = token_repo
        self.password_hasher = password_hasher

    def register(self, email: str, password: str):
        if not email or not password:
            raise ValueError("Invalid data")

        if self.user_repo.find_by_email(email):
            raise ValueError("User already exists")

        hashed = self.password_hasher.hash(password)
        user = self.user_repo.create(email, hashed)

        return user

