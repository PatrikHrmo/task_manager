import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from main import add_task_db, update_task_db


# Positive test: The test changes the state from default to in_progress, and is successful if there is a task with id number 1.
@pytest.mark.update_positive
@pytest.mark.parametrize("name, task, state", [
        ("Name 1", "Task 1", "in_progress"),
        ("Name 1", "Task 1", "done")
    ])
def test_update_task_db_positive(test_db, name, task, state):
    add_task_db(test_db, name, task)
    test_db.cursor.execute("SELECT id FROM tasks WHERE name = %s AND task = %s", (name, task))
    position = test_db.cursor.fetchone()
    task_id = position[0]
    result = update_task_db(test_db, task_id, state)
    assert result is True


# Negative test: The test is successful if at least one of the values is empty: the state of the task is not updated.
@pytest.mark.update_negative
@pytest.mark.parametrize("state, task_id", [
        ("in_progress", None),
        ("", None)
    ])
def test_update_task_db_negative(test_db, state, task_id):
    with pytest.raises(ValueError):
        update_task_db(test_db, state, task_id)