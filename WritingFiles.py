#!/usr/bin/python

#!Writing Files

my_file = open("file path", "a")
print(my_file.write("Enter the Text You Need....."))

#!We add some text at the end of the file,,,,,, But be careful cause you can mess up the file at the same time if you run the code more than once

my_file.close()


#!Over-writing a file

my_file = open("file path", "w")
print(my_file.write("Enter your text....."))
my_file.close()


#!Writing in HTML
my_file = open("file path to index.html", "w")
print(my_file.write("<body> This is HTML written using Python </body>"))

#!Go ahead and test it out!!!!
