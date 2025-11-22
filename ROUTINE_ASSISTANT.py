import json
import random
from datetime import datetime

# Data for tips & quotes

PRODUCTIVITY_TIPS = [
    "Break big tasks into small steps.",
    "Avoid multitasking — focus on one task.",
    "Use timers to stay disciplined.",
    "Start with the hardest task first.",
    "Write your tasks the night before."
]

MOTIVATIONAL_QUOTES = [
    "Success is built on consistent small actions.",
    "Discipline beats motivation.",
    "You are improving — keep going.",
    "Your future self will thank you.",
    "Every step counts, no matter how small."
]


# Task Manager Class

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task_name):
        task = {
            "task": task_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "done": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\n Task added: {task_name}")

    def view_tasks(self):
        if not self.tasks:
            print("\n No tasks yet.")
            return

        print("\n Your Tasks:")
        for i, t in enumerate(self.tasks, 1):
            status = "✓ Done" if t["done"] else " Pending"
            print(f"{i}. {t['task']} | {status} | Added: {t['created_at']}")

    def mark_done(self, index):
        try:
            self.tasks[index]["done"] = True
            self.save_tasks()
            print(f"\n Task marked as done: {self.tasks[index]['task']}")
        except IndexError:
            print("\n Invalid task number.")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"\n Removed: {removed['task']}")
        except IndexError:
            print("\n Invalid task number.")



# Help Functions


def show_menu():
    print("\n==============================")
    print("  SMART DAILY ROUTINE ASSISTANT")
    print("==============================")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove a task")
    print("5. Productivity tip")
    print("6. Motivational quote")
    print("7. Exit")
    print("==============================")

def random_tip():
    print("\n Productivity Tip:")
    print(random.choice(PRODUCTIVITY_TIPS))

def random_quote():
    print("\n Motivation:")
    print(random.choice(MOTIVATIONAL_QUOTES))


# Main App Logic


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                manager.add_task(task)
            else:
                print(" Task cannot be empty.")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            num = int(input("Task number to mark as done: ")) - 1
            manager.mark_done(num)

        elif choice == "4":
            num = int(input("Task number to remove: ")) - 1
            manager.remove_task(num)

        elif choice == "5":
            random_tip()

        elif choice == "6":
            random_quote()

        elif choice == "7":
            print("\n Goodbye! Stay productive.")
            break

        else:
            print("\n Invalid option. Try again.")

# Run the app
main()
