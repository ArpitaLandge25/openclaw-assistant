import os
import shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            if file.endswith(".pdf"):
                dest = os.path.join(folder_path, "PDFs")
            elif file.endswith(".py"):
                dest = os.path.join(folder_path, "Python")
            elif file.endswith(".jpg"):
                dest = os.path.join(folder_path, "Images")
            else:
                dest = os.path.join(folder_path, "Others")

            os.makedirs(dest, exist_ok=True)
            shutil.move(file_path, os.path.join(dest, file))
    
    print("Files Organized Successfully!")