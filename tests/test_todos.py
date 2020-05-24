import pytest

import random

from models.todos import ToDos

"""
Tests for get Todo API.
"""

@pytest.mark.parametrize('expected_count', [200])
def test_todos_count(api_end_point, expected_count):
    """
    Check count of todos.
    """

    response = api_end_point.todos.get_todos()
    assert response.status_code == 200

    actual_count = len(response.json())
    assert actual_count == expected_count


@pytest.mark.parametrize('expected_todo_id', [1, 99, 100, 101, 199, 200])
def test_todos_by_id(api_end_point, expected_todo_id):
    """
    Boundary value analysis for get by id.
    """

    response = api_end_point.todos.get_todos_by_id(todo_id=expected_todo_id)
    assert response.status_code == 200
    todos = ToDos(response.json())
    assert todos.id == expected_todo_id


@pytest.mark.parametrize('expected_length', [0])
@pytest.mark.parametrize('expected_todo_id', [0, 201])
def test_todos_invalid_input(api_end_point, expected_length, expected_todo_id):
    """
    Check the handling for invalid id
    """

    response = api_end_point.todos.get_todos_by_id(todo_id=expected_todo_id)
    assert response.status_code == 404

    actual_length = len(response.json())
    assert actual_length == expected_length


@pytest.mark.parametrize('expected_todo_id', [random.randrange(1, 200, 1)])
def test_response_structure_for_valid_random_id(api_end_point, expected_todo_id):
    """
    Validating response structure for a random id.
    """

    response = api_end_point.todos.get_todos_by_id(todo_id=expected_todo_id)
    assert response.status_code == 200
    todos = ToDos(response.json())
    assert todos.id == expected_todo_id
    assert todos.user_id is not None
    assert len(todos.title) != 0
    assert todos.completed is not None


