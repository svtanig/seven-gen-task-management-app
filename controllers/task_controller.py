#Connect db and cli

from database.db_handler import DBHandler
from models.task import Task

# TaskController handles the business logic for task management
# It interacts with the DBHandler to perform CRUD operations on tasks
# It also serves as an interface for the CLI to interact with tasks
# This class is responsible for creating, listing, updating, deleting, and marking tasks as completed
class TaskController:
    def __init__(self):
        self.db = DBHandler()

    def create_task(self, title, desc, due, priority):
        task = Task(title, desc, due, priority)
        self.db.add_task(task)

    def list_tasks(self, filter_type=None, filter_value=None):
        if filter_type:
            return self.db.list_tasks({filter_type: filter_value})
        return self.db.list_tasks()

    def update_task(self, task_id, updates):
        self.db.update_task(task_id, updates)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

    def mark_completed(self, task_id):
        self.db.mark_completed(task_id)
