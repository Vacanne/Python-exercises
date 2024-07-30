import os

# Initialize the list of tasks
tasks = []

def add_task():
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})
    print(f'Task "{title}" added.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['title']} [{status}]")

def mark_task_completed():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f'Task "{tasks[task_number - 1]["title"]}" marked as completed.')
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["title"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
