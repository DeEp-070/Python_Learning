#opening a file
#file = open("data.txt")
#reading
#content = file.read()
#print(content)
#closing file
# file.close()
#
# So the traditional pattern is:
#
# file = open("data.txt", "r")
#
# content = file.read()
#
# print(content)
#
# file.close()
# The with statement
#
# Use:
#
# with open("data.txt", "r") as file:
#     content = file.read()
#
# print(content)

# | Mode  | Meaning         |
# | ----- | --------------- |
# | `"r"` | Read            |
# | `"w"` | Write           |
# | `"a"` | Append          |
# | `"x"` | Create new file |
# | `"b"` | Binary mode     |
# | `"t"` | Text mode       |

#Reading line by line
# with open("products.txt", "r") as file:
#     for line in file:
#         print(line)
# However, you'll notice an extra newline because each line already contains its newline character.
#
# Use:
#
# with open("products.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# read(), readline(), readlines()
# read()
#
# Reads the entire file:
#
# content = file.read()
# readline()
#
# Reads one line:
#
# line = file.readline()
# readlines()
#
# Reads all lines into a list:
#
# lines = file.readlines()

# Writing multiple lines
#
# You can write a complete string:
#
# with open("products.txt", "w") as file:
#     file.write("Laptop\n")
#     file.write("Mouse\n")
#     file.write("Keyboard\n")
#
# Or:
#
# products = ["Laptop\n", "Mouse\n", "Keyboard\n"]
#
# with open("products.txt", "w") as file:
#     file.writelines(products)
#
# writelines() does not automatically insert newlines.
#
# That's why the strings above contain \n.

# Encoding
#
# For text files, explicitly specifying an encoding is a good professional habit:
#
# with open("data.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#
# And:
#
# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write("বাংলা এবং Python")
#
# UTF-8 handles a very broad range of Unicode text.

# Handling missing files
#
# Consider:
#
# with open("users.txt", "r", encoding="utf-8") as file:
#     data = file.read()
#
# If the file doesn't exist:
#
# FileNotFoundError
#
# You can handle it:
#
# try:
#     with open("users.txt", "r", encoding="utf-8") as file:
#         data = file.read()
# except FileNotFoundError:
#     print("users.txt does not exist.")

# pathlib — modern path handling
#
# Instead of manually constructing:
#
# "D:\\Python_Learning\\data\\users.txt"
#
# use:
#
# from pathlib import Path
#
# path = Path("data") / "users.txt"
#
# Then:
#
# with path.open("r", encoding="utf-8") as file:
#     data = file.read()
#
# You can also simply use:
#
# data = path.read_text(encoding="utf-8")
#
# and:
#
# path.write_text("Hello Python", encoding="utf-8")

# Checking whether a path exists
# from pathlib import Path
#
# path = Path("data/users.txt")
#
# if path.exists():
#     print("File exists")
# else:
#     print("File doesn't exist")
#
# You can distinguish:
#
# path.is_file()
# path.is_dir()

# Creating directories
# from pathlib import Path
#
# data_dir = Path("data")
#
# data_dir.mkdir(exist_ok=True)
#
# Now the directory exists.
#
# For nested directories:

# Path("data/orders/2026").mkdir(parents=True, exist_ok=True)

# Listing files
# from pathlib import Path
#
# data_dir = Path("testPath")
#
# for path in data_dir.iterdir():
#     print(path)
#
# You can filter:
#
# for file in data_dir.glob("*.json"):
#     print(file)

# JSON

import json

user = {
    "name": "Ajay",
    "age": 21,
    "skills": ["Python", "SQL", "FastAPI"]
}
# json_data = json.dumps(user)  #python -> json
# print(type(json_data)) #output <class str>
#
# data = json.loads(json_data) #json -> python
# print(type(data)) #output <class dict>

# #Writing JSON to a file
# with open("user.json",'w',encoding="utf_8") as file:
#     json.dump(user , file , indent=4)

# # Reading JSON
# with open("user.json",'r',encoding="utf-8") as file:
#     user_convert = json.load(file)
# print(user_convert)

#csv
#writing csv
import csv
# rows =  [
#     ["name", "age", "course"],
#     ["Ajay", 21, "BCA"],
#     ["Riya", 22, "BCA"]
# ]
# with open("Students.csv","w",newline="",encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)
# #reading csv
# with open("Students.csv","r",newline="",encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for data in reader:
#         print(data)

# DictReader
# For structured CSV data, DictReader is often more convenient.
# with open("Students.csv","r",newline="",encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for data in reader:
#         print(data["name"],data["age"],data["course"])


