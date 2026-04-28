# File Organizer Script
# Copyright (c) 2026 Roshan Jeffrin
# Licensed under the MIT License
import os, shutil, zipfile
from tkinter import Tk
from pathlib import Path
from tkinter import filedialog

# Optional imports (only if installed)
try:
    import rarfile
except ImportError:
    rarfile = None

try:
    import py7zr
except ImportError:
    py7zr = None


def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


def extract_rar(file_path, extract_to):
    if rarfile is None:
        print(f"[!] rarfile module not installed. Skipping {file_path.name}")
        return
    with rarfile.RarFile(file_path) as rar_ref:
        rar_ref.extractall(extract_to)


def extract_7z(file_path, extract_to):
    if py7zr is None:
        print(f"[!] py7zr module not installed. Skipping {file_path.name}")
        return
    with py7zr.SevenZipFile(file_path, mode="r") as z:
        z.extractall(path=extract_to)


def process_archives(directory):
    directory = Path(directory)

    for file in directory.iterdir():
        if file.is_file():
            suffix = file.suffix.lower()

            if suffix in [".zip", ".rar", ".7z"]:
                folder_name = file.stem
                target_folder = directory / folder_name

                print(f"[+] Processing: {file.name}")

                # Create folder
                target_folder.mkdir(exist_ok=True)

                # Move file into folder
                new_path = target_folder / file.name
                shutil.move(str(file), str(new_path))

                # Extract based on type
                try:
                    if suffix == ".zip":
                        extract_zip(new_path, target_folder)
                    elif suffix == ".rar":
                        extract_rar(new_path, target_folder)
                    elif suffix == ".7z":
                        extract_7z(new_path, target_folder)

                    print(f"[✓] Done: {file.name}")

                except Exception as e:
                    print(f"[✗] Error processing {file.name}: {e}")


if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide main window

    folder_path = filedialog.askdirectory(title="Select Folder Containing Archives")

    if folder_path:
        process_archives(folder_path)
    else:
        print("No folder selected.")
