import os

# join strings with appropriate system specific file separator
os.path.join("folder1", "folder2", "folder3", "file.png")

# stores the system specific file separator
os.sep

# cd or getwd() is 
os.getcwd()

os.chdir()

os.path.abspath("file_notes.py")

# Does the path include root
os.path.isabs()

# relative path from path1 to path2
os.path.relpath()

os.path.dirname() # Directories in path
os.path.basename() # file in path

os.path.exists()
os.path.isfile()
os.path.isdir()
os.path.getsize() # size in bytes as an integer
os.listdir() # list of strings with files and folder


