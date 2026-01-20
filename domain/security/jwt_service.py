import jwt
import time
import os

class JwtService:
    JWT_EXPIRES_IN = int(os.getenv("JWT_EXPIRES_IN", 3600))
    JWT_SECRET = os.getenv("JWT_SECRET", "changeme")

    def generate(self, user_id: str):
        expires_at = int(time.time()) + self.JWT_EXPIRES_IN
        payload = {
            "sub": user_id,
            "exp": expires_at
        }

        token = jwt.encode(
            payload,
            self.JWT_SECRET,
            algorithm="HS256"
        )

        return token, self.JWT_EXPIRES_IN

    def validate(self, token: str):
        return jwt.decode(
            token,
            self.JWT_SECRET,
            algorithms=["HS256"]
        )


