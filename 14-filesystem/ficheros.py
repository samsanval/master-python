from io import open
import pathlib
import shutil
import os

# Open file
# file = open('textFile.txt', "a+")

path = str(pathlib.Path().absolute()) + "/textFile.txt"
print(path)
file = open(path, "a+")

# Write in file
# file.write('Texto a escribir')
# Close file
file.close()

# Read content
fileRead = open(path, "r")
content = fileRead.read()
print(content)

# Read content and store it in a list
list = fileRead.readline()
fileRead.close()
print(list)

# Copy
"""
pathCopy = str(pathlib.Path().absolute()) + "/textFileCopy.txt"
shutil.copyfile(path, pathCopy)
"""
# Move
pathCopy = str(pathlib.Path().absolute()) + "/textFileMoved.txt"
shutil.move(path,pathCopy)

# Remove
pathCopy = str(pathlib.Path().absolute()) + "/textFileCopy.txt"

if os.path.isfile(pathCopy):
    os.remove(pathCopy)
else:
    print('No existe el fichero')
