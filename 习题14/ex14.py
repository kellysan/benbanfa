#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex14
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-06
#    Change Activity:  2019-03-06:

from sys import argv

script, user_name = argv

prompt = "===>"

print("Hi %s , I'm the %s scripts." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
    Alright, so you said %s about liking me.
    you live in %s. Not sure where that is.
    And you have a %s computer. Nice.
""" %(likes, lives, computer))