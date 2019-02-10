#!/usr/bin/python

#!Reading from External Files in python

open("file path", "the action")


#!On the file path you have to type out the path of the file you want to open e.g " ~/usr/share/Docs/readme.txt"
#!On the action you have to type out the action you want
#!In python "r"--> read, "w"-->write, "a"-->append, "r+"-->read and write

my_file = open("file path", "r")

#!close a file
my_file.close()

#!if possible to read the file
print(my_file.readable())

#!Read the file
print(my_file.read())

#!Read a specific line
print(my_file.readline())

#!Read every line and put them in a list
print(my_file.readlines())

#!Use in a for loop
my_file = open("file path", "r+")
for sales in my_file.readlines():
    print(sales)
my_file.close()

#!Go ahead and test it out!!!!
