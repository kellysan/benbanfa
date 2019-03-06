#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex7
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-06
#    Change Activity:  2019-03-06:

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3 ,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))