#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex8
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-07
#    Change Activity:  2019-03-07:


def print_two(*args):
    arg1, arg2 = args
    print("arg1: %s, arg2:%s" %(arg1, arg2))

def print_two_again(arg1,arg2):
    print("arg1: %s, arg2: %s" %(arg1, arg2))

def print_one(arg1):
    print("arg1: %s" % arg1)

def print_none():
    print("I got nothing'.")


print_two("Zend", "Shaw")
print_two_again("Zend", "Shaw")
print_one("Zend")
print_none()