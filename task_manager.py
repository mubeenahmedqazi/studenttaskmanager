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

def main():
    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()