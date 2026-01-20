import grpc
from concurrent import futures
from adapters.inbound.grpc.grpc_server import GrpcServer
from adapters.outbound.mongo.user_repository import MongoUserRepository
from adapters.outbound.redis.token_repository import RedisTokenRepository
from domain.services.auth_service import AuthService
from domain.security.password_hasher import PasswordHasher
import pymongo, redis, os
import auth_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    db = mongo_client.get_default_database()
    users_collection = db.users

    redis_client = redis.Redis.from_url(
        os.getenv("REDIS_URL"),
        decode_responses=True
    )

    auth_service = AuthService(
        MongoUserRepository(users_collection),
        RedisTokenRepository(redis_client),
        PasswordHasher()
    )

    auth_pb2_grpc.add_AuthServiceServicer_to_server(
        GrpcServer(auth_service), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
