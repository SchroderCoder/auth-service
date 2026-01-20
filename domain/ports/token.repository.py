from abc import ABC, abstractmethod

class TokenRepository(ABC):
    def store(self, token: str, user_id: str, ttl: int):
        pass

    def exists(self, token: str) -> bool:
        pass

    def delete(self, token: str):
        pass
