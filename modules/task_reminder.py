def add_task():
    task = input("Enter task: ")

    with open("data/tasks.txt", "a") as f:
        f.write(task + "\n")

    print("Task Added!")

def show_tasks():
    print("\nYour Tasks:")
    with open("data/tasks.txt", "r") as f:
        print(f.read())