#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex16
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-06
#    Change Activity:  2019-03-06:

from sys import argv,exit


script, filename = argv

print("We're going to erase %s." % filename)
print("If you don't want that, hit CTRL + C (^C)")
print("If you do want that,hit RETURN")

flag = input("Y or N")
if flag == "Y":


print("Opening the file ...")
target = open(filename,"w")
print("Truncation the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, We close it.")
target.close()

