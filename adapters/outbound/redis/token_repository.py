class RedisTokenRepository:
    def __init__(self, redis_client):
        self.redis = redis_client

    def store(self, token, user_id, ttl):
        self.redis.setex(token, ttl, user_id)

    def exists(self, token):
        return self.redis.exists(token)

    def delete(self, token):
        self.redis.delete(token)
