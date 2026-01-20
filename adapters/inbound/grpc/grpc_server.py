import grpc
import auth_pb2
import auth_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp

class GrpcServer(auth_pb2_grpc.AuthServiceServicer):

    def __init__(self, auth_service):
        self.auth_service = auth_service

    def Register(self, req, ctx):
        try:
            user = self.auth_service.register(req.email, req.password)

            ts = Timestamp()
            ts.GetCurrentTime()

            return auth_pb2.RegisterReply(
                user_id=user["id"],
                created_at=ts
            )
        except ValueError as e:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
