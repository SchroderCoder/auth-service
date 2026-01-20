import bcrypt
from typing import Union

class PasswordHasher:
    def hash(self, password: Union[str, bytes]) -> bytes:
        if isinstance(password, str):
            password = password.encode("utf-8")
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def verify(self, password: Union[str, bytes], hashed: bytes) -> bool:
        if isinstance(password, str):
            password = password.encode("utf-8")
        return bcrypt.checkpw(password, hashed)

