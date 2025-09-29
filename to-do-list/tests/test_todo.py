import json
from pathlib import Path
import tempfile
import os

from to_do import add_task, list_tasks, complete_task, delete_task, clear_tasks, load_tasks


def test_add_and_list(tmp_path):
    p = tmp_path / "tasks.json"
    t = add_task(p, "Write tests")
    assert t.id == 1
    tasks = list_tasks(p)
    assert len(tasks) == 1
    assert tasks[0].title == "Write tests"


def test_complete_and_delete(tmp_path):
    p = tmp_path / "tasks.json"
    add_task(p, "Task A")
    add_task(p, "Task B")
    t = complete_task(p, 1)
    assert t is not None
    assert t.done is True
    tasks_all = load_tasks(p)
    assert sum(1 for x in tasks_all if x.done) == 1
    deleted = delete_task(p, 2)
    assert deleted is not None
    remaining = load_tasks(p)
    assert len(remaining) == 1


def test_clear(tmp_path):
    p = tmp_path / "tasks.json"
    add_task(p, "One")
    add_task(p, "Two")
    clear_tasks(p)
    tasks = load_tasks(p)
    assert tasks == []
