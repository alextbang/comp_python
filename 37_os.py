# sample os methods
import os

# shutil can perform more 'dangerous' operations than OS module
import shutil

# list contents of the test-directory
a = os.listdir("test-directory")
print(a)

# get current working directory path
print(os.getcwd())

# check if a file exists
print(os.path.exists("textfile.txt"))

###


# this will remove an entire directory--use with caution
shutil.rmtree("dir")

