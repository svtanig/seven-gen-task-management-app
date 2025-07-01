#Task attributes and logic

import datetime
import uuid


# Task Model
class Task:
    def __init__(self, title, description, due_date, priority):
        self.task_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        return self.__dict__
