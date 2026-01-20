import jwt, time, os

class JwtService:
    def generate(self, user_id: str):
        expires_at = int(time.time()) + int(os.getenv("JWT_EXPIRES_IN"))
        payload = {
            "sub": user_id,
            "exp": expires_at
        }
        return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256") , expires_at

    def validate(self, token: str):
        return jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])

