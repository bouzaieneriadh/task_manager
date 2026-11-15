"""Task Manager - Part 1 (console application).

Features: add a task, display tasks, search tasks by keyword, exit.
"""

tasks = []  # list of task titles; the task number is its position + 1


def show_menu():
    print()
    print("=== TASK MANAGER ===")
    print("1. Add a task  2. Display  3. Search  0. Exit")


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


def search_tasks():
    keyword = input("Keyword: ").strip().lower()
    if keyword == "":
        print("Error: the keyword cannot be empty.")
        return
    found = False
    for number, title in enumerate(tasks, start=1):
        if keyword in title.lower():
            print(f"{number}. {title}")
            found = True
    if not found:
        print("No task found.")


def main():
    running = True
    while running:
        show_menu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "0":
            print("Goodbye!")
            running = False
        else:
            print("Error: invalid option. Please choose 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()
