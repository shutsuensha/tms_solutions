import os
import shutil
import platform
from pathlib import Path
from collections import defaultdict

def get_size_in_gb(size_bytes):
    """Helper function to convert bytes to gigabytes."""
    return size_bytes / (1024 ** 3)

def main():
    # Print the name of the OS
    print(f"Operating System: {platform.system()}")

    # Print the current directory
    current_path = Path.cwd()
    print(f"Current Directory: {current_path}")

    # Dictionary to hold files by extension
    files_by_ext = defaultdict(list)

    # Collect files by extension
    for file in current_path.iterdir():
        if file.is_file():
            ext = file.suffix
            files_by_ext[ext].append(file)

    # Sort files into extension-based folders and move them
    for ext, files in files_by_ext.items():
        # Skip files with .py extension
        if ext == '.py':
            continue

        folder_name = ext[1:].upper() + "_FILES"
        target_folder = current_path / folder_name
        target_folder.mkdir(exist_ok=True)

        total_size = 0
        for file in files:
            file_size = file.stat().st_size
            total_size += file_size
            shutil.move(str(file), target_folder)

        # Output message about sorted files and their size in BYTES
        # For output message with GB replace {total_size} on {get_size_in_gb(total_size):.2f}
        print(f"In folder '{folder_name}', {len(files)} file(s) were moved with a total size of {total_size} bytes")

        # Rename at least one file in the folder
        renamed_file = list(target_folder.iterdir())[0]
        new_name = f"renamed_{renamed_file.name}"
        renamed_path = target_folder / new_name
        renamed_file.rename(renamed_path)
        print(f"File '{renamed_file.name}' was renamed to '{new_name}'")

if __name__ == "__main__":
    main()
