#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex20
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-07
#    Change Activity:  2019-03-07:


import  sys
#from sys import  argv
#argv 传入参数解包
script, input_file = sys.argv
#script, input_file = argv

#打印文件所有内容
def print_all(f):
    print(f.read())


#将文件游标重置
def rewind(f):
    f.seek(0)


#读取文件每一行
def print_a_line(line_count, f):
    print(line_count, f.readline())


#创建一个文件打开对象
current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines")

current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
