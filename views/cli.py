from controllers.task_controller import TaskController
import datetime


class CLI:
    def __init__(self):
        self.controller = TaskController()

    def menu(self):
        while True:
            print("\n--- Task Manager ---\n")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Update Task")
            print("4. Mark Task Completed")
            print("5. Delete Task")
            print("6. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.mark_task_completed()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.")

    # --------------------------
    # Add Task
    # --------------------------
    def add_task(self):
        details = self.collect_task_details()
        if not details:
            print("⚠️ Task creation cancelled.\n")
            return

        print("\n📋 Please review your task details:")
        print(f"🆔 Title       : {details['title']}")
        print(f"📝 Description : {details['description']}")
        print(f"📅 Due Date    : {details['due_date']}")
        print(f"⭐ Priority    : {details['priority']}")

        confirm = input("✅ Save this task? (y/n): ").strip().lower()
        if confirm == 'y':
            self.controller.create_task(
                details['title'],
                details['description'],
                details['due_date'],
                details['priority']
            )
            print("✅ Task added successfully!\n")
        else:
            print("❌ Invalid input. Task not saved.\n")

    def collect_task_details(self):
        title = self.get_non_empty_input("Title")
        if title is None:
            return None

        description = self.get_non_empty_input("Description")
        if description is None:
            return None

        due_date = self.get_valid_due_date()
        if due_date is None:
            return None

        priority = self.get_priority_choice()
        if priority is None:
            return None

        return {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority
        }
    
    def list_tasks(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("📭 No tasks found.\n")
            return

        print("\n📝 Task List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"\n[{idx}] Title      : {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Due Date   : {task['due_date']}")
            print(f"    Priority   : {task['priority']}")
            print(f"    Status     : {task['status']}")
            print(f"    Created At : {task['created_at']}")
            print(f"    ID         : {task['_id']}")
            print("    " + "-" * 30 + "\n")
            

    def update_task(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("📭 No tasks available to update.")
            return

        self.list_tasks()
        try:
            choice = int(input("\nEnter task number to update (or 0 to cancel): "))
            if choice == 0:
                print("⚠️ Update cancelled.")
                return
            if not 1 <= choice <= len(tasks):
                print("❌ Invalid task number.")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        task_id = tasks[choice - 1]["_id"]

        fields = {
            "1": ("title", "Title"),
            "2": ("desc", "Description"),
            "3": ("due_date", "Due Date"),
            "4": ("priority", "Priority"),
            "5": ("status", "Status")
        }

        print("\nWhich field do you want to update?")
        print("1. Title")
        print("2. Description")
        print("3. Due Date")
        print("4. Priority")
        print("5. Status")

        field_choice = input("Enter your choice (1-5): ").strip()
        if field_choice not in fields:
            print("❌ Invalid field choice.")
            return

        field_key, field_name = fields[field_choice]

        # Field-specific validation
        if field_key in ["title", "desc"]:
            value = self.get_non_empty_input(f"New {field_name}")
            if value is None:
                print("⚠️ Update cancelled.")
                return

        elif field_key == "due_date":
            value = self.get_valid_due_date()
            if value is None:
                print("⚠️ Update cancelled.")
                return

        elif field_key == "priority":
            value = self.get_priority_choice()
            if value is None:
                print("⚠️ Update cancelled.")
                return

        elif field_key == "status":
            value = self.get_status_choice()
            if value is None:
                print("⚠️ Update cancelled.")
                return

        self.controller.update_task(task_id, {field_key: value})
        print("✅ Task updated.")


    def mark_task_completed(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("📭 No tasks to mark as completed.")
            return

        self.list_tasks()
        try:
            choice = int(input("\nEnter task number to mark as completed (or 0 to cancel): "))
            if choice == 0:
                print("⚠️ Operation cancelled.")
                return
            if not 1 <= choice <= len(tasks):
                print("❌ Invalid task number.")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        task_id = tasks[choice - 1]["_id"]
        self.controller.mark_completed(task_id)
        print("✅ Task marked as completed.")


    def delete_task(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("📭 No tasks to delete.")
            return

        self.list_tasks()
        try:
            choice = int(input("\nEnter task number to delete (or 0 to cancel): "))
            if choice == 0:
                print("⚠️ Deletion cancelled.")
                return
            if not 1 <= choice <= len(tasks):
                print("❌ Invalid task number. Deletion cancelled.")
                return
        except ValueError:
            print("❌ Please enter a valid number. Deletion cancelled.")
            return

        confirm = input("❗ Are you sure you want to delete this task? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Invalid Input. Deletion cancelled.")
            return

        task_id = tasks[choice - 1]["_id"]
        self.controller.delete_task(task_id)
        print("🗑️ Task deleted.")



    # --------------------------
    # Input Helpers
    # --------------------------
    def get_non_empty_input(self, prompt):
        while True:
            value = input(f"{prompt} (or type 'c' to cancel): ").strip()
            if value.lower() == 'c':
                return None
            if value:
                return value
            print("❌ This field cannot be empty.\n")

    def get_valid_due_date(self):
        while True:
            due = input("Due Date (YYYY-MM-DD) or type 'c' to cancel: ").strip()
            if due.lower() == "c":
                return None
            try:
                datetime.datetime.strptime(due, "%Y-%m-%d")
                return due
            except ValueError:
                print("❌ Invalid date format. Please enter as YYYY-MM-DD.\n")

    def get_priority_choice(self):
        priorities = {"1": "Low", "2": "Medium", "3": "High"}
        while True:
            print("Priority Options:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            choice = input("Choose a priority (1/2/3) or 'c' to cancel: ").strip()
            if choice.lower() == 'c':
                return None
            if choice in priorities:
                return priorities[choice]
            print("❌ Invalid choice. Please choose 1, 2, or 3.\n")

    def get_status_choice(self):
        statuses = {"1": "Pending", "2": "In Progress", "3": "Completed"}
        while True:
            print("Status Options:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")
            choice = input("Choose a status (1/2/3) or 'c' to cancel: ").strip()
            if choice.lower() == 'c':
                return None
            if choice in statuses:
                return statuses[choice]
            print("❌ Invalid choice. Please choose 1, 2, or 3.\n")


    


