import pytest
import bcrypt


def test_login_success(auth_service, user_repo, token_repo):
    password = "password"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user_repo.find_by_email.return_value = type(
        "User", (), {"id": "123", "password": hashed}
    )()

    token_repo.store.return_value = None

    result = auth_service.login("test@test.com", password)

    assert "access_token" in result
    assert "expires_in" in result
    token_repo.store.assert_called_once()


def test_login_wrong_password(auth_service, user_repo):
    user_repo.find_by_email.return_value = type(
        "User", (), {"password": b"wrong"}
    )()

    with pytest.raises(ValueError):
        auth_service.login("test@test.com", "password")


def test_login_user_not_found(auth_service, user_repo):
    user_repo.find_by_email.return_value = None

    with pytest.raises(ValueError):
        auth_service.login("test@test.com", "password")
