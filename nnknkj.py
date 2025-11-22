# SMART DAILY ROUTINE ASSISTANT
import random
import time

# --------------------------
# DATA
# --------------------------

productivity_tips = [
    "Break big tasks into small steps.",
    "Avoid multitasking — focus on one task.",
    "Use timers to stay disciplined.",
    "Remove distractions for 10 minutes and start.",
    "Write your tasks the night before."
]

motivational_quotes = [
    "Success is built on consistent small actions.",
    "You are improving every single day.",
    "Discipline beats motivation.",
    "Your future self will thank you.",
    "Keep going — you’re closer than you think."
]

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")


# --------------------------
# MAIN PROGRAM
# --------------------------

def main():
    tasks = load_tasks()

    print("\n===== SMART DAILY ROUTINE ASSISTANT =====")

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Remove a task")
        print("5. Get a productivity tip")
        print("6. Get a motivational quote")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark!")
            else:
                num = int(input("Task number to mark done: "))
                if 1 <= num <= len(tasks):
                    print(f"Good job finishing: {tasks[num-1]}!")
                    tasks[num-1] += " ✓"
                    save_tasks(tasks)
                else:
                    print("Invalid number")

        elif choice == "4":
            if not tasks:
                print("No tasks to remove!")
            else:
                num = int(input("Task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number")

        elif choice == "5":
            print("\n💡 Productivity Tip:")
            print(random.choice(productivity_tips))

        elif choice == "6":
            print("\n🔥 Motivation:")
            print(random.choice(motivational_quotes))

        elif choice == "7":
            print("Goodbye! Stay productive.")
            break

        else:
            print("Invalid choice, try again.")


main()
