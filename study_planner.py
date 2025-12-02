import json
import os

DATA_FILE = "study_data.json"

# ------------------ DATA HANDLING ------------------

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ TASK FUNCTIONS ------------------

def add_task(data):
    print("\n--- ADD NEW TASK ---")
    title = input("Task title: ")
    subject = input("Subject: ")
    duration = int(input("Estimated duration (minutes): "))
    priority = input("Priority (Low/Medium/High): ")

    task = {
        "title": title,
        "subject": subject,
        "duration": duration,
        "priority": priority,
        "completed": False
    }

    data["tasks"].append(task)
    save_data(data)
    print("Task added successfully!\n")

def view_tasks(data, filter_by=None):
    print("\n--- TASK LIST ---")
    for i, task in enumerate(data["tasks"], start=1):
        if filter_by == "pending" and task["completed"]:
            continue
        if filter_by == "completed" and not task["completed"]:
            continue

        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{i}. {task['title']} | {task['subject']} | {task['duration']} mins | {task['priority']} | {status}")
    print()

def mark_completed(data):
    view_tasks(data, filter_by="pending")
    task_num = int(input("Enter task number to mark as completed: "))
    if 1 <= task_num <= len(data["tasks"]):
        data["tasks"][task_num - 1]["completed"] = True
        save_data(data)
        print("Task marked as completed!\n")
    else:
        print("Invalid number.\n")

# ------------------ ANALYTICS ------------------

def show_stats(data):
    print("\n--- STUDY STATS ---")
    total_completed = sum(task["completed"] for task in data["tasks"])
    total_minutes = sum(task["duration"] for task in data["tasks"] if task["completed"])

    print(f"Total tasks completed: {total_completed}")
    print(f"Total hours studied: {total_minutes / 60:.2f} hours\n")

    # Subject breakdown
    subjects = {}
    for task in data["tasks"]:
        if task["completed"]:
            subjects[task["subject"]] = subjects.get(task["subject"], 0) + 1

    print("Completed tasks per subject:")
    for subject, count in subjects.items():
        print(f" - {subject}: {count}")
    print()

# ------------------ MAIN MENU ------------------

def main():
    data = load_data()

    while True:
        print("=== SMART STUDY PLANNER ===")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Mark task as completed")
        print("6. View study stats")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(data)
        elif choice == "2":
            view_tasks(data)
        elif choice == "3":
            view_tasks(data, "pending")
        elif choice == "4":
            view_tasks(data, "completed")
        elif choice == "5":
            mark_completed(data)
        elif choice == "6":
            show_stats(data)
        elif choice == "7":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
