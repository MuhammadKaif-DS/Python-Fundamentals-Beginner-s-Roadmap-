# File Handling in Python means working with files 
# Reading from them, Writing to them, Creating new ones, or Deleting existing ones.
# It’s an essential part of Python programming because it allows you to store data permanently.

# 1.Opening a File
#In Python, you use the built-in open() function.
# example: like this
file = open("filename", "mode")

# Common Modes:
'r'	# Read (default)error if file doesn’t exist
'w'	# Write – creates a new file or overwrites existing
'a'	# Append – adds data to the end of file
'x'	# Create – creates a new file, error if exists
'r+'# Read and write

# 2.Reading from a File
file = open("file.txt", "r")
file.readline()  # Reads one line
file.readlines() # Reads all lines as a list
file.read()      # Reads all lines as a list
file.close()     # Close file
 # 3.Writing to a File
file = open("file.txt", "w")
file.write("Hello, Python!\n")
file.close()
# Append data (without overwriting):
file = open("example.txt", "a")
file.write("This line added.\n")
file.close()

# 4.Using with Statement (Recommended)
# Using with automatically closes the file.
with open("example.txt", "r") as file:
    data = file.read()
    print(data)

# 5.Checking if File Exists
import os # os module stands for Operating System

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")

# 6.Deleting a File
import os
os.remove("example.txt")