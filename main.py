"""Task Manager - first version (add, display, menu only)."""

tasks = []


def show_menu():
    print()
    print("=== TASK MANAGER ===")
    print("1. Add a task  2. Display  0. Exit")


def add_task():
    title = input("Task title: ").strip()
    if title == "":
        print("Error: the title cannot be empty.")
        return
    tasks.append(title)
    print("Task added successfully.")


def display_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for number, title in enumerate(tasks, start=1):
        print(f"{number}. {title}")


def main():
    running = True
    while running:
        show_menu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "0":
            print("Goodbye!")
            running = False
        else:
            print("Error: invalid option. Please choose 0, 1 or 2.")


if __name__ == "__main__":
    main()
