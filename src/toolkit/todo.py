import json


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task not in self.tasks:
            raise ValueError(f"Task not found: {task}")
        self.tasks.remove(task)

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f)

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.tasks = json.load(f)