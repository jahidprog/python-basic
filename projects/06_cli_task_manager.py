import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Tasks ---")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "

        print(f"{i}. [{status}] {task['title']}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)

            print("✅ Task completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)

            print(f"🗑️ Deleted: {removed['title']}")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


def show_pending(tasks):
    pending = [task for task in tasks if not task["completed"]]

    print("\n--- Pending Tasks ---")

    if not pending:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']}")


def show_completed(tasks):
    completed = [task for task in tasks if task["completed"]]

    print("\n--- Completed Tasks ---")

    if not completed:
        print("No completed tasks.")
        return

    for i, task in enumerate(completed, start=1):
        print(f"{i}. {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Pending Tasks")
        print("6. Completed Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            show_pending(tasks)

        elif choice == "6":
            show_completed(tasks)

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()