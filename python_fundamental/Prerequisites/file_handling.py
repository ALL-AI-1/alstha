# File Handling Course in Python

# 1. Writing to a file (overwriting)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "w") as f:
        f.write("This is a new file content.\n")
        f.write("Welcome to the file handling course!\n")
except Exception as e:
    print("Error in writing (overwrite):", e)

# 2. Appending to a file
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "a") as f:
        f.write("This line is appended.\n")
        f.write("hi\n")
except Exception as e:
    print("Error in appending:", e)

# 3. Reading the entire file
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        content = f.read()
        print("Full file content:\n", content)
except Exception as e:
    print("Error in reading:", e)

# 4. Reading file line by line
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("Reading line by line:")
        for line in f:
            print(line.strip())
except Exception as e:
    print("Error in line-by-line reading:", e)

# 5. Reading specific number of lines (e.g., first 5 lines)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("First 5 lines:")
        for i in range(5):
            line = f.readline()
            if not line:
                break
            print(line.strip())
except Exception as e:
    print("Error in reading specific lines:", e)

# 6. Searching for a word in the file (e.g., 'alstha')
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("Lines containing 'alstha':")
        for line in f:
            if "alstha" in line:
                print(line.strip())
except Exception as e:
    print("Error in searching for word:", e)

# 7. Using 'with' statement is recommended for file handling (already shown above)

# 8. Deleting a file
import os
file_path = r"F:/REAL_PROJECTS/All_AI/temp_file.txt"
# Create a temp file to demonstrate deletion
try:
    with open(file_path, "w") as f:
        f.write("This file will be deleted.\n")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} deleted successfully.")
    else:
        print(f"{file_path} does not exist.")
except Exception as e:
    print("Error in deleting file:", e)

# 9. Handling file not found error
try:
    with open(r"F:/REAL_PROJECTS/All_AI/non_existent.txt", "r") as f:
        pass
except FileNotFoundError:
    print("File not found error handled.")

# 10. Reading all lines into a list
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        lines = f.readlines()
        print("All lines as a list:", lines)
except Exception as e:
    print("Error in readlines():", e)

# 11. Copying a file
import shutil
src = r"F:/REAL_PROJECTS/All_AI/text.txt"
dst = r"F:/REAL_PROJECTS/All_AI/text_copy.txt"
try:
    shutil.copy(src, dst)
    print(f"Copied {src} to {dst}")
except Exception as e:
    print("Error in copying file:", e)

# 12. Renaming a file
try:
    old_name = r"F:/REAL_PROJECTS/All_AI/text_copy.txt"
    new_name = r"F:/REAL_PROJECTS/All_AI/text_renamed.txt"
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} to {new_name}")
    else:
        print(f"{old_name} does not exist for renaming.")
except Exception as e:
    print("Error in renaming file:", e)

# 13. Getting file information (size, last modified time)
import time
file_info_path = r"F:/REAL_PROJECTS/All_AI/text.txt"
try:
    if os.path.exists(file_info_path):
        size = os.path.getsize(file_info_path)
        mtime = os.path.getmtime(file_info_path)
        print(f"File size: {size} bytes")
        print("Last modified:", time.ctime(mtime))
    else:
        print(f"{file_info_path} does not exist for info.")
except Exception as e:
    print("Error in getting file info:", e)

# 14. Reading and writing binary files
binary_file = r"F:/REAL_PROJECTS/All_AI/binary_file.bin"
try:
    # Write binary data
    with open(binary_file, "wb") as f:
        f.write(b'\x00\x01\x02\x03\x04')
    # Read binary data
    with open(binary_file, "rb") as f:
        data = f.read()
        print("Binary data read:", data)
except Exception as e:
    print("Error in binary file handling:", e)

# 15. Using contextlib for file context management (advanced)
from contextlib import contextmanager

@contextmanager
def open_file_context(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

try:
    with open_file_context(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("First line using contextlib context manager:", f.readline().strip())
except Exception as e:
    print("Error using contextlib context manager:", e)

# 16. Checking if a file exists before reading
file_to_check = r"F:/REAL_PROJECTS/All_AI/text.txt"
if os.path.isfile(file_to_check):
    print(f"{file_to_check} exists and is a file.")
else:
    print(f"{file_to_check} does not exist or is not a file.")

# 17. Listing all files in a directory
directory = r"F:/REAL_PROJECTS/All_AI"
try:
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print("Files in directory:", files)
except Exception as e:
    print("Error listing files in directory:", e)

# 18. Truncating a file (removing all content but keeping the file)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r+") as f:
        f.truncate(0)
        print("File truncated (content removed).")
except Exception as e:
    print("Error in truncating file:", e)

# 19. Reading a file using 'with' and exception handling in one line (Python 3.10+)
# (This is a demonstration; if using older Python, skip this)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f: print("First char:", f.read(1))
except Exception as e:
    print("Error in one-line with-read:", e)

# 20. File pointer operations (seek, tell)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "w+") as f:
        f.write("abcdefg")
        f.seek(0)
        print("File pointer at:", f.tell())
        print("First 3 chars:", f.read(3))
        print("File pointer now at:", f.tell())
except Exception as e:
    print("Error in file pointer operations:", e)

# 21. Reading file as an iterator (next)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "w") as f:
        f.write("line1\nline2\nline3\n")
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("First line using next():", next(f).strip())
        print("Second line using next():", next(f).strip())
except Exception as e:
    print("Error using file as iterator:", e)

# 22. Safely closing a file (if not using 'with')
try:
    f = open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r")
    print("First line (manual close):", f.readline().strip())
except Exception as e:
    print("Error in manual open:", e)
finally:
    try:
        f.close()
    except:
        pass

# 23. Writing multiple lines at once (writelines)
try:
    lines_to_write = ["alpha\n", "beta\n", "gamma\n"]
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "w") as f:
        f.writelines(lines_to_write)
    print("Multiple lines written using writelines().")
except Exception as e:
    print("Error in writelines():", e)

# 24. Reading file using list comprehension
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        stripped_lines = [line.strip() for line in f]
        print("Lines using list comprehension:", stripped_lines)
except Exception as e:
    print("Error in list comprehension read:", e)

# 25. File encoding (reading/writing with utf-8)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/utf8.txt", "w", encoding="utf-8") as f:
        f.write("नमस्ते, Alstha!\n")
    with open(r"F:/REAL_PROJECTS/All_AI/utf8.txt", "r", encoding="utf-8") as f:
        print("UTF-8 file content:", f.read())
except Exception as e:
    print("Error in utf-8 file handling:", e)

# 26. Reading a file in chunks (useful for large files)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("Reading file in 4-byte chunks:")
        while True:
            chunk = f.read(4)
            if not chunk:
                break
            print(repr(chunk))
except Exception as e:
    print("Error in chunked reading:", e)

# 27. Temporary files (using tempfile module)
import tempfile
try:
    with tempfile.NamedTemporaryFile(delete=True, mode="w+t") as tempf:
        tempf.write("Temporary file content.\n")
        tempf.seek(0)
        print("Temp file content:", tempf.read())
        print("Temp file name:", tempf.name)
except Exception as e:
    print("Error with tempfile:", e)

# # 28. File locking (platform dependent, advanced)
# # Note: File locking is not natively cross-platform in Python's stdlib.
# # On Windows, use msvcrt; on Unix, use fcntl. Here is a simple demonstration for Unix:
# import sys
# if sys.platform != "win32":
#     try:
#         import fcntl
#         with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r+") as f:
#             fcntl.flock(f, fcntl.LOCK_EX)
#             print("File locked (Unix only).")
#             fcntl.flock(f, fcntl.LOCK_UN)
#     except Exception as e:
#         print("Error in file locking (Unix):", e)
# else:
#     print("File locking demo skipped on Windows.")

# 29. Reading CSV files (basic)
import csv
csv_file = r"F:/REAL_PROJECTS/All_AI/sample.csv"
try:
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Alice", 30])
        writer.writerow(["Bob", 25])
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        print("CSV file content:")
        for row in reader:
            print(row)
except Exception as e:
    print("Error in CSV file handling:", e)

# 30. JSON file handling (read/write)
import json
json_file = r"F:/REAL_PROJECTS/All_AI/sample.json"
data = {"name": "Alstha", "age": 5, "skills": ["Python", "AI"]}
try:
    with open(json_file, "w") as f:
        json.dump(data, f)
    with open(json_file, "r") as f:
        loaded = json.load(f)
        print("JSON loaded:", loaded)
except Exception as e:
    print("Error in JSON file handling:", e)

# 31. Pickle file handling (serialize/deserialize Python objects)
import pickle
pickle_file = r"F:/REAL_PROJECTS/All_AI/sample.pkl"
obj = {"a": 1, "b": 2}
try:
    with open(pickle_file, "wb") as f:
        pickle.dump(obj, f)
    with open(pickle_file, "rb") as f:
        loaded_obj = pickle.load(f)
        print("Pickle loaded:", loaded_obj)
except Exception as e:
    print("Error in Pickle file handling:", e)

# 32. Reading file with error handling for encoding issues
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r", encoding="utf-8") as f:
        print("Read with utf-8 encoding:", f.read())
except UnicodeDecodeError:
    print("Unicode decode error handled.")
except Exception as e:
    print("Other error in encoding read:", e)

# 33. File permissions (checking and changing)
try:
    file_perm = r"F:/REAL_PROJECTS/All_AI/text.txt"
    if os.path.exists(file_perm):
        print("File permissions (octal):", oct(os.stat(file_perm).st_mode)[-3:])
        # Change to read-only
        os.chmod(file_perm, 0o444)
        print("Changed to read-only.")
        # Change back to read-write
        os.chmod(file_perm, 0o666)
        print("Changed to read-write.")
    else:
        print("File does not exist for permission demo.")
except Exception as e:
    print("Error in file permission handling:", e)

# 34. Directory creation and deletion
dir_path = r"F:/REAL_PROJECTS/All_AI/new_folder"
try:
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print("Directory created:", dir_path)
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
        print("Directory deleted:", dir_path)
except Exception as e:
    print("Error in directory creation/deletion:", e)

# 35. Reading file using pathlib (modern Python)
from pathlib import Path
try:
    p = Path(r"F:/REAL_PROJECTS/All_AI/text.txt")
    if p.exists():
        print("File content using pathlib:", p.read_text())
    else:
        print("File does not exist for pathlib demo.")
except Exception as e:
    print("Error in pathlib file handling:", e)

# 36. File context manager (custom, advanced)
from contextlib import ContextDecorator

class CustomFileOpener(ContextDecorator):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"CustomFileOpener: Opened {self.filename}")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"CustomFileOpener: Closed {self.filename}")

try:
    with CustomFileOpener(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        print("First line (custom context manager):", f.readline().strip())
except Exception as e:
    print("Error in custom context manager:", e)

# 37. File reading with try-except-else-finally
try:
    f = open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r")
except Exception as e:
    print("Error opening file:", e)
else:
    print("File opened successfully (try-except-else-finally).")
    print("First line:", f.readline().strip())
finally:
    try:
        f.close()
    except:
        pass

# 38. File reading with enumerate (line numbers)
try:
    with open(r"F:/REAL_PROJECTS/All_AI/text.txt", "r") as f:
        for idx, line in enumerate(f, 1):
            print(f"Line {idx}: {line.strip()}")
except Exception as e:
    print("Error in enumerate reading:", e)

# 39. File existence and type check (isfile, isdir)
try:
    path = r"F:/REAL_PROJECTS/All_AI/text.txt"
    if os.path.isfile(path):
        print(f"{path} is a file.")
    elif os.path.isdir(path):
        print(f"{path} is a directory.")
    else:
        print(f"{path} does not exist.")
except Exception as e:
    print("Error in file/directory check:", e)

# 40. File reading with contextlib.suppress (ignore errors)
from contextlib import suppress
with suppress(FileNotFoundError):
    with open(r"F:/REAL_PROJECTS/All_AI/non_existent.txt", "r") as f:
        print(f.read())

# End of full file handling in Python!
