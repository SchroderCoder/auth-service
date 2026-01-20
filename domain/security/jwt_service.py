import jwt, time, os

class JwtService:
    def generate(self, user_id: str):
        payload = {
            "sub": user_id,
            "exp": int(time.time()) + 3600
        }
        return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

    def validate(self, token: str):
        return jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
