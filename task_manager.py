tasks = []

def add_task(title):
    tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})
    print(f"Task '{title}' added!")

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['title']} [{status}]")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task {task_id} marked as completed.")
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    initial_len = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < initial_len:
        print(f"Task {task_id} deleted successfully.")
    else:
        print("Error: Task ID not found.")

def main():
    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            tid = int(input("Enter task ID to complete: "))
            complete_task(tid)
        elif choice == "4":
            try:
                tid = int(input("Enter task ID to delete: "))
                delete_task(tid)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()