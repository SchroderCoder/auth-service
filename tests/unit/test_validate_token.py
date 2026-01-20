import pytest


def test_validate_token_success(auth_service, token_repo):
    token_repo.exists.return_value = True

    token, _ = auth_service.jwt_service.generate("123")

    user_id = auth_service.validate_token(token)

    assert user_id == "123"


def test_validate_token_invalid(auth_service, token_repo):
    token_repo.exists.return_value = False

    with pytest.raises(ValueError):
        auth_service.validate_token("invalid")


def test_validate_token_no_token(auth_service):
    with pytest.raises(ValueError):
        auth_service.validate_token("")
