import pytest
from app import connect


def test_connection():
    assert connect() == "Not Connected" or connect() == "ELM Connected" or connect() = "OBD Connected" or connect() = "Car Connected"
