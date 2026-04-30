import os

def search_files(folder, keyword):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))