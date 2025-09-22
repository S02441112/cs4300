import pytest
from homework1.src.task7 import get_status_code

def test_status_code_failure(monkeypatch):
    def mock_get():
        raise ConnectionError("Failed to connect")

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(ConnectionError):
        get_status_code("http://bad-url.com")