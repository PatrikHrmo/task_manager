import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from db_connect import DbTaskManager

@pytest.fixture(scope="function")
def test_db():
    with DbTaskManager("localhost", "root", "1111", None) as conn:
        conn.db_create()
    with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
        conn.db_table_create()

    with DbTaskManager("localhost", "root", "1111", "tasks") as db:
        yield db
        db.cursor.execute("DELETE FROM tasks")
        db.connection.commit()