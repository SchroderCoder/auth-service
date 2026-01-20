def test_logout_success(auth_service, token_repo):
    auth_service.logout("token")
    token_repo.delete.assert_called_once_with("token")


def test_logout_idempotent(auth_service, token_repo):
    auth_service.logout("token")
    auth_service.logout("token")

    assert token_repo.delete.call_count == 2


def test_logout_invalid_data(auth_service):
    import pytest

    with pytest.raises(ValueError):
        auth_service.logout("")
