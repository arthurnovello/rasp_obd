import pytest
from app import connect


def test_connection():
    assert connect() == "Not Connected"
