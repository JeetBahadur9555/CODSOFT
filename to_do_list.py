# A simple command-line To-Do List

# Initialize the list of tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number!")

# Function to update a task
def update_task(task_number, new_task):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = new_task
        print(f"Updated task {task_number} to: {new_task}")
    else:
        print("Invalid task number!")

# Main loop
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_number, new_task)
        elif choice == '5':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
