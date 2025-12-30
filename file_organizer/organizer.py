import os
import shutil

def organize_files(directory):
    """
    Organizes files in the given directory by file extension.
    Skips folders and files without extensions.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        # Skip files without extensions
        if "." not in filename:
            continue

        extension = filename.split(".")[-1].lower()
        target_dir = os.path.join(directory, f"{extension}_files")

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        shutil.move(file_path, os.path.join(target_dir, filename))


if __name__ == "__main__":
    path = input("Enter the directory path to organize: ")
    organize_files(path)
