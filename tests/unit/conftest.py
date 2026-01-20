import pytest
from unittest.mock import MagicMock
from domain.services.auth_service import AuthService
from domain.security.jwt_service import JwtService
from domain.security.password_hasher import PasswordHasher


@pytest.fixture
def user_repo():
    return MagicMock()


@pytest.fixture
def token_repo():
    return MagicMock()


@pytest.fixture
def auth_service(user_repo, token_repo):
    return AuthService(
        user_repo=user_repo,
        token_repo=token_repo,
        password_hasher=PasswordHasher(),
        jwt_service=JwtService()
    )
