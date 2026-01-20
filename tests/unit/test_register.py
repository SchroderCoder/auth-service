import pytest


def test_register_success(auth_service, user_repo):
    user_repo.find_by_email.return_value = None
    user_repo.create.return_value = type(
        "User", (), {"id": "123"}
    )()

    user = auth_service.register("test@test.com", "password")

    assert user.id == "123"
    user_repo.create.assert_called_once()


def test_register_existing_user(auth_service, user_repo):
    user_repo.find_by_email.return_value = True

    with pytest.raises(ValueError):
        auth_service.register("test@test.com", "password")


def test_register_invalid_data(auth_service):
    with pytest.raises(ValueError):
        auth_service.register("", "")
