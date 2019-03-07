#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex15
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-06
#    Change Activity:  2019-03-06:


# 导入sys模块中 argv 函数
from sys import argv


#解包，将argv 获取的参数分给两个参数
script, filename = argv

#打开一个文件，并创建一个文件对象
txt = open(filename)

#打您文件内容
print("Here's your file %r." % filename)
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

# 重新读取文件内容
print(txt_again.read())
txt_again.close()
