import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from db_connect import DbTaskManager

@pytest.fixture(scope="function")
def test_db():
    conn = DbTaskManager("localhost", "root", "1111", "tasks")
    conn.db_create()
    conn.db_table_create()
    yield conn
    conn.db_connect()
    conn.cursor.execute("DELETE FROM tasks")
    conn.connection.commit()
    conn.db_close()