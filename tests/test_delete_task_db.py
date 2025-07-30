import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from main import add_task_db, delete_task_db


# Positive test: Deletes a row in the table tasks after adding one.
@pytest.mark.delete_positive
@pytest.mark.parametrize("name, task", [("Name 1", "Task 1")])
def test_delete_task_db_positive(test_db, name, task):
    test_db.cursor.execute("INSERT INTO tasks (name, task) VALUES (%s, %s)", (name, task))
    test_db.connection.commit()
    test_db.cursor.execute("SELECT id FROM tasks WHERE name = %s AND task = %s", (name, task))
    position = test_db.cursor.fetchone()
    task_id = position[0]
    success = delete_task_db(test_db, task_id)
    assert success is True


# Negative test: The test passes when there is missing value of task_id, so nothing happens.
@pytest.mark.delete_negative
@pytest.mark.parametrize("task_id", [
        None,
        0
    ])
def test_delete_task_db_negative(test_db, task_id):
    with pytest.raises(ValueError):
        delete_task_db(test_db, task_id)