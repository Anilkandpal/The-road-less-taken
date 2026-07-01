import os
import sys

print(os.getcwd())  # gives the current working directory
print(
    os.listdir()
)  # gives the list of files and directories in the current working directory
os.mkdir("new_directory")  # creates a new directory in the current working directory

os.rmdir("new_directory")  # removes the directory

print(sys.version)  # gives the version of python installed
print(sys.platform)  # gives the platform on which python is running
print(sys.path)  # gives the list of directories where python looks for modules
print("start")
# sys.exit()  # exits the program
print("end")  # this line will not be executed because of sys.exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
print(
    "sum = ", a + b
)  # if you go to the termanl and run this commant - python "3 - all fundamentals.py" 10 20 it will run this programm and the sum will be printed
# however   if you run this program in the vs code it will give an error because it is not able to find the arguments 10 and 20. To fix this we can use the following code
