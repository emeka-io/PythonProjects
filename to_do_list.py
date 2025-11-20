# ------------------------------
# SIMPLE TO-DO LIST APP (BEGINNER PROJECT)
# ------------------------------

# A list to store tasks
tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            choice = int(input("\nEnter the task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    option = input("Choose an option (1-4): ")

    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        delete_task()
    elif option == "4":
        print("Goodbye! Thanks for using the To-Do App.")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")
