from unittest.mock import patch, Mock
from pytest_mock import MockerFixture
from dummy_functions import check_file_exists, get_user_data


# Section: Using unittest.mock.patch
def test_check_file_exists_manual_patch() -> None:
    filepath = "/path/to/some/file.txt"

    patcher = patch("dummy_functions.os.path.exists")
    mock_exists = patcher.start()

    mock_exists.return_value = True

    try:
        result = check_file_exists(filepath=filepath)
        mock_exists.assert_called_once_with(filepath)
        assert result is True
    finally:
        patcher.stop()


def test_check_file_exists_context_manager() -> None:
    filepath = "/path/to/some/file.txt"

    with patch("dummy_functions.os.path.exists") as mock_exists:
        mock_exists.return_value = True

        result = check_file_exists(filepath=filepath)
        mock_exists.assert_called_once_with(filepath)
        assert result is True


@patch("dummy_functions.os.path.exists")
def test_check_file_exists_decorator(mock_exists: Mock) -> None:
    filepath = "/path/to/some/file.txt"

    mock_exists.return_value = True

    result = check_file_exists(filepath=filepath)
    mock_exists.assert_called_once_with(filepath)
    assert result is True


def test_check_file_pytest_mocker(mocker: MockerFixture) -> None:
    filepath = "/path/to/some/file.txt"

    mock_exists = mocker.patch("dummy_functions.os.path.exists")
    mock_exists.return_value = True

    result = check_file_exists(filepath=filepath)
    mock_exists.assert_called_once_with(filepath)
    assert result is True


# Section: MagicMock and Configuring Mock Objects
def test_get_user_data_success(mocker: MockerFixture) -> None:
    mock_api_response: dict[str, str | int] = {
        "id": 1,
        "name": "test user",
    }

    mock_get = mocker.patch("dummy_functions.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_api_response

    data = get_user_data(user_id=1)

    mock_get.assert_called_once_with(
        "https://api.example.com/users/1"
    )
    assert data == mock_api_response
