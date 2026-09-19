# Mini Project: CLI Todo App

tasks = []


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter task: ").strip()

    if task:
        tasks.append(task)
        print("Task added.")


def remove_task():
    show_tasks()

    if not tasks:
        return

    try:
        index = int(input("Task number to remove: "))
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    while True:
        print("\n--- TODO ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
