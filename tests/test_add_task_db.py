import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from main import add_task_db


# Positive test: The test is successful if both name 1 and task 1 are added into the table.
@pytest.mark.add_positive
@pytest.mark.parametrize("name_1, task_1",[("Name 1", "Task 1")])
def test_add_task_db_positive(test_db, name_1, task_1):
    result = add_task_db(name_1, task_1)
    assert result is True


# Negative test: The test is successful if at least one of the name 2 or task 2 is empty: nothing will be added into the table.
@pytest.mark.add_negative
@pytest.mark.parametrize("name_2, task_2",[
        ("Name 2", ""),
        ("", ""),
        ("", "Task 2")
    ])
def test_add_task_db_negative(test_db, name_2, task_2):
    with pytest.raises(ValueError):
        add_task_db(name_2, task_2)