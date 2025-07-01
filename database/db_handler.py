#Database operations (CRUD)

from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

class DBHandler:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("DB_NAME")] #from .env
        self.collection = self.db["tasks"]

    def add_task(self, task):
        self.collection.insert_one(task.to_dict())

    def list_tasks(self, filters={}):
        return list(self.collection.find(filters))

    def update_task(self, task_id, updates):
        self.collection.update_one({"_id": ObjectId(task_id)}, {"$set": updates})

    def delete_task(self, task_id):
        self.collection.delete_one({"_id": ObjectId(task_id)})

    def mark_completed(self, task_id):
        self.update_task(task_id, {"status": "Completed"})
