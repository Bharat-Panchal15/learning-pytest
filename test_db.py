from db import Database
import pytest

@pytest.fixture
def db():
    database = Database()
    yield database
    database.data.clear()

def test_add_user(db):
    db.add_user(1,"Bharat")
    assert db.get_user(1) == "Bharat"

def test_duplicate_user(db):
    db.add_user(1,"Bharat")
    with pytest.raises(ValueError,match="User already exists"):
        db.add_user(1,"Lucky")

def test_delete_user(db):
    db.add_user(1,"Bharat")
    db.delete_user(1)
    assert db.get_user(1) is None