class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        """Add a new task to the to-do list"""
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added successfully!")
        else:
            print(f"Task '{task_name}' already exists!")

    def delete_task(self, task_name):
        """Delete a task from the to-do list"""
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def mark_task_completed(self, task_name):
        """Mark a task as completed"""
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed!")
        else:
            print(f"Task '{task_name}' not found!")

    def view_tasks(self):
        """View all tasks in the to-do list"""
        print("To-Do List:")
        for task, status in self.tasks.items():
            status = "Completed" if status else "Pending"
            print(f"- {task}: {status}")


def main():
    todo = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            todo.delete_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            todo.mark_task_completed(task_name)
        elif choice == "4":
            todo.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
