import os
import shutil
import send2trash


f = open("practice.txt", "w+")
f.write("This is a test string")
f.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir("/Users"))

shutil.move("practice.txt", "/Users/seanshea/PythonClass")
