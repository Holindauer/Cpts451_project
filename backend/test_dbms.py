import pytest
from dbms import Database

def test_first_customer_id():
    db = Database("database.db")
    assert db._new_customer_id() == 0

def test_no_customer_found():
    db = Database("database.db")
    assert db._does_customer_exist("test") == False

def test_no_admin_found():
    db = Database("database.db")
    assert db._does_admin_exist("test") == False

