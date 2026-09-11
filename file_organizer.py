#!/usr/bin/env python3
"""
Smart File Organizer

A beginner-friendly command-line script that organizes files in a folder
into subfolders based on their file type/extension.
"""

import shutil
from pathlib import Path


# Categories mapped to their file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"],
}


def get_category(file_path):
    """
    Return the category folder name for a given file based on its extension.
    Files with no extension or unknown extensions go to 'Others'.
    """
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination_folder, file_name):
    """
    Return a unique file path inside destination_folder.
    If a file with the same name already exists, append _1, _2, etc.
    """
    destination = destination_folder / file_name

    if not destination.exists():
        return destination

    # Split filename into stem and suffix
    stem = Path(file_name).stem
    suffix = Path(file_name).suffix

    counter = 1
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        destination = destination_folder / new_name

        if not destination.exists():
            return destination

        counter += 1


def organize_folder(folder_path):
    """
    Organize files in the given folder into category subfolders.
    Returns a summary dictionary.
    """
    scanned = 0
    moved = 0
    skipped = 0
    category_counts = {}

    # Make sure the folder exists
    if not folder_path.exists():
        print(f"Error: The folder '{folder_path}' does not exist.")
        return None

    if not folder_path.is_dir():
        print(f"Error: The path '{folder_path}' is not a folder.")
        return None

    # Go through each item in the folder
    for item in folder_path.iterdir():
        # Skip directories, only process files
        if not item.is_file():
            continue

        scanned += 1

        try:
            category = get_category(item)
            category_counts[category] = category_counts.get(category, 0) + 1

            # Create category folder if it doesn't exist
            destination_folder = folder_path / category
            destination_folder.mkdir(exist_ok=True)

            # Find a safe destination name
            destination = get_unique_destination(destination_folder, item.name)

            # Move the file
            shutil.move(str(item), str(destination))
            moved += 1

        except Exception as error:
            print(f"Warning: Could not move '{item.name}': {error}")
            skipped += 1

    return {
        "scanned": scanned,
        "moved": moved,
        "skipped": skipped,
        "category_counts": category_counts,
    }


def print_summary(summary):
    """Display a clear summary of the organization results."""
    if summary is None:
        return

    print("\n" + "=" * 40)
    print("Organization Complete!")
    print("=" * 40)
    print(f"Files scanned: {summary['scanned']}")
    print(f"Files moved:   {summary['moved']}")
    print(f"Files skipped: {summary['skipped']}")
    print("-" * 40)
    print("Files in each category:")

    for category in sorted(summary["category_counts"]):
        count = summary["category_counts"][category]
        print(f"  {category}: {count}")

    print("=" * 40)


def main():
    """Main function that runs the file organizer."""
    print("Welcome to Smart File Organizer!")
    print("This script will organize files in a folder by their type.\n")

    # Ask user for folder path
    folder_input = input("Enter the path of the folder to organize: ").strip()

    # Remove quotes if the user pasted a path with surrounding quotes
    folder_input = folder_input.strip('"').strip("'")

    folder_path = Path(folder_input).expanduser().resolve()

    summary = organize_folder(folder_path)
    print_summary(summary)

    if summary is not None:
        print("\nDone! Your files have been organized.")


if __name__ == "__main__":
    main()
