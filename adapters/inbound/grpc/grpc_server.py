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
                user_id=user.id,
                created_at=ts
            )
        except ValueError as e:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    def Login (self, req, ctx):
        try:
            result = self.auth_service.login(req.email, req.password)

            return auth_pb2.LoginReply(
                access_token = result["access_token"],
                expires_in = result["expires_in"]
            )
        
        except ValueError as e:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    def ValidateToken(self, request, ctx):
        try:
            user_id = self.auth_service.validate_token(request.token)

            return auth_pb2.ValidateTokenReply(
                is_valid = True,
                user_id = user_id
            ) 
        
        except ValueError as e:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))


    def Logout(self, request, ctx):
        try:
            self.auth_service.logout(request.token)

            return auth_pb2.LogoutReply(
                status = "logged out"
            )
        
        except ValueError as e:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))