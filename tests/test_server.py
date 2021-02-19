import os
import pytest
import sys

from falcon import testing

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app


@pytest.fixture()
def client():
    return testing.TestClient(app)


def test_get_message(client):
    result = client.simulate_get('/ping')
    assert result.json == 'pong!'
