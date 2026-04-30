from modules.file_organizer import organize_files
from modules.learning_tracker import add_learning_entry
from modules.resume_builder import generate_resume_points
from modules.search_tool import search_files
from modules.task_reminder import add_task, show_tasks

print("\n--- OpenClaw Smart Assistant ---")

print("1. Organize Files")
print("2. Add Learning")
print("3. Generate Resume Points")
print("4. Search Files")
print("5. Add Task")
print("6. Show Tasks")

choice = input("Choose option: ")

if choice == "1":
    folder = input("Enter folder path: ")
    organize_files(folder)

elif choice == "2":
    add_learning_entry()

elif choice == "3":
    folder = input("Enter project folder: ")
    generate_resume_points(folder)

elif choice == "4":
    folder = input("Enter folder: ")
    keyword = input("Enter keyword: ")
    search_files(folder, keyword)

elif choice == "5":
    add_task()

elif choice == "6":
    show_tasks()

else:
    print("Invalid choice")