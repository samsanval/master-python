import os
# import shutil

if not os.path.isdir('./myFolder'):
    os.mkdir('./myFolder')
path = './myFolder'
pathNew = './myFolder_Copy'
# shutil.copytree(path, pathNew)
if os.path.isdir('./myFolder_Copy'):
    os.rmdir(pathNew)

content = os.listdir(path)
for file in content:
    print(file)