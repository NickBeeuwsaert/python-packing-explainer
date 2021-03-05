import pytest
from main import index
from pyramid import testing


def test_index():
    with testing.testConfig() as config:
        assert index(testing.DummyRequest()) == "Hello, world!"
