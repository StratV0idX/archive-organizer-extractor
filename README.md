# 📂 File Organizer & Archive Extractor

A Python-based automation tool that organizes and extracts archive files (`.zip`, `.rar`, `.7z`) into structured folders. This script helps keep directories clean by automatically grouping and extracting compressed files.

---

## Features

- Automatically detects archive files in a selected directory  
- Creates a separate folder for each archive  
- Moves archive files into their respective folders  
- Extracts contents automatically  
- Supports multiple formats:
  - ZIP (built-in support)
  - RAR (optional)
  - 7Z (optional)  
- Gracefully handles missing dependencies  

---

## Tech Stack

- Python 3  
- Standard Libraries:
  - `os`
  - `shutil`
  - `zipfile`
  - `pathlib`
  - `tkinter`
- Optional Libraries:
  - `rarfile`
  - `py7zr`

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/archive-organizer-extractor.git
cd archive-organizer-extractor
```
### 2. Install optional dependencies
```bash
pip install rarfile py7zr
```
### 3. Run the script:
```bash
python main.py
```
## Example

### Before:
```
folder/
  ├── project.zip
  ├── data.rar
  ├── backup.7z
```
### After:
```
folder/
  ├── project/
  │      ├── project.zip
  │      └── extracted files...
  ├── data/
  │      ├── data.rar
  │      └── extracted files...
  ├── backup/
  │      ├── backup.7z
  │      └── extracted files...
```
## 👨‍💻 Author

Roshan Jeffrin R
