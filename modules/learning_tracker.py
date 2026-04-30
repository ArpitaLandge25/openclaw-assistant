from datetime import datetime

def add_learning_entry():
    entry = input("What did you learn today? ")

    with open("data/learning_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {entry}\n")

    print("Learning saved!")