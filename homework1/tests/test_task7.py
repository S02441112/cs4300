import pytest
from src.task7 import get_status_code

def test_status_code_failure(monkeypatch):
    """
    Test simulates failed network request by replacing (monkeypatching)
    requests.get with mock function that always raises ConnectionError.

    Expected behavior: get_status_code should raise a ConnectionError.
    """
    def mock_get(url):
        raise ConnectionError("Failed to connect")

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(ConnectionError):
        get_status_code("http://bad-url.com")

def test_get_status_code():
    """
    Test makes HTTP request to https://example.com that confirms response is HTTP 200.
    """
    # Example.com should always return 200 - OK
    assert get_status_code("https://example.com") == 200