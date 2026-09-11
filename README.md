# Smart File Organizer

A simple command-line Python script that automatically organizes files in a selected folder into subfolders based on their file type or extension.

## Features

- Organizes files into categories: **Images**, **Documents**, **Videos**, **Audio**, **Archives**, **Code**, and **Others**.
- Automatically creates category folders if they do not already exist.
- Handles duplicate filenames safely — never overwrites existing files.
- Ignores subfolders and only organizes files directly inside the selected folder.
- Provides a clear summary after organizing, including total files scanned, moved, skipped, and counts per category.

## Technologies Used

- Python 3
- Python standard library only:
  - `pathlib` — for working with file and folder paths
  - `shutil` — for moving files

## How It Works

1. The script asks you to enter a folder path.
2. It checks that the folder exists and is a valid directory.
3. It scans each file directly inside the folder.
4. It determines the category for each file based on its extension.
5. It creates the category folder if it does not already exist.
6. It moves the file into the correct category folder.
7. If a file with the same name already exists in the destination folder, the script renames the new file by appending `_1`, `_2`, and so on.
8. It prints a summary when finished.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the `file-organizer` folder.
3. Run the script:

```bash
python file_organizer.py
```

4. Enter the path of the folder you want to organize when prompted.

## Example Usage

```bash
$ python file_organizer.py
Welcome to Smart File Organizer!
This script will organize files in a folder by their type.

Enter the path of the folder to organize: /Users/aisha/Downloads

========================================
Organization Complete!
========================================
Files scanned: 12
Files moved:   12
Files skipped: 0
----------------------------------------
Files in each category:
  Archives: 1
  Audio: 2
  Code: 2
  Documents: 3
  Images: 3
  Others: 1
========================================

Done! Your files have been organized.
```

## Example Before/After Folder Structure

### Before

```
Downloads/
├── photo.jpg
├── assignment.pdf
├── song.mp3
├── program.py
├── unknown.xyz
├── report.docx
├── video.mp4
├── archive.zip
└── notes.txt
```

### After

```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   ├── assignment.pdf
│   ├── report.docx
│   └── notes.txt
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Archives/
│   └── archive.zip
├── Code/
│   └── program.py
└── Others/
    └── unknown.xyz
```

## Screenshots

Below are example screenshots showing the script in action. You can add your own by saving them in a `screenshots/` folder inside this project.

### Terminal Output

Replace this with a screenshot of the terminal showing the summary after running the script.

![Terminal output showing organization summary](screenshots/terminal-output.png)

### Before Organizing

Replace this with a screenshot of the folder before running the script.

![Folder before organizing](screenshots/before-organizing.png)

### After Organizing

Replace this with a screenshot of the folder after running the script.

![Folder after organizing](screenshots/after-organizing.png)

## Important Safety Note


This script **moves files** from one location to another. It does not delete or overwrite files, but it does change your folder structure. Always test it on a copy of your files or a sample folder first to make sure it behaves the way you expect.