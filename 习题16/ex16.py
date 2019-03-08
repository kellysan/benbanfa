#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex16
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-06
#    Change Activity:  2019-03-06:

#导入系统sys模块 中argv 方法
from sys import argv,exit

#导入时间模块
import time


#解包传入参数，script 第一个是脚本名称，filename 第二个是命令行第一个参数
script, filename = argv

#打印数据
print("We're going to erase %s." % filename)
print("If you don't want that, hit CTRL + C (^C)")
print("If you do want that,hit RETURN")

#睡眠3秒
time.sleep(3)

# 以下只有在python2中可以实现,输入回车可以跳过，python3中不可以
#raw_input("?")


print("Opening the file ...")

#创建一个文件打开对象
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

