import pytest
from toolkit.todo import TodoList


@pytest.fixture
def todo():
    return TodoList()


def test_new_list_is_empty(todo):
    assert todo.tasks == []


def test_add_task(todo):
    todo.add_task("buy milk")
    assert todo.tasks == ["buy milk"]


def test_add_multiple_tasks(todo):
    todo.add_task("buy milk")
    todo.add_task("study pytest")
    assert todo.tasks == ["buy milk", "study pytest"]


def test_remove_task(todo):
    todo.add_task("buy milk")
    todo.remove_task("buy milk")
    assert todo.tasks == []


def test_remove_missing_task_raises_error(todo):
    with pytest.raises(ValueError):
        todo.remove_task("dance")


def test_save_and_load(todo, tmp_path):
    todo.add_task("buy milk")
    todo.add_task("study pytest")
    file = tmp_path / "tasks.json"

    todo.save(file)

    new_todo = TodoList()
    new_todo.load(file)
    assert new_todo.tasks == ["buy milk", "study pytest"]


def test_load_missing_file_raises_error(todo, tmp_path):
    with pytest.raises(FileNotFoundError):
        todo.load(tmp_path / "does_not_exist.json")