import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from main import update_task_db


# Positive test: The test changes the state from default to in_progress, and is successful if there is a task with id number 1.
@pytest.mark.positive
@pytest.mark.parametrize("state, task_id",
        [
            ("in_progress", 1)
        ]
)

def test_update_task_db_positive(state, task_id):

    assert update_task_db(state, task_id)


# Negative test: The test is successful if at least one of the values is empty: the state of the task is not updated.
@pytest.mark.negative
@pytest.mark.parametrize("state, task_id",
        [
            ("in_progress", 1)
        ]
)

def test_update_task_db_negative(state, task_id):

    with pytest.raises(ValueError):
        update_task_db(state, task_id)