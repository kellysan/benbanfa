#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       练习1
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-05
#    Change Activity:  2019-03-05:

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are,", cars,"cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty car today")
print("we can transport", carpool_capacity, "pepole today")
print("we have", passengers, "to  carpool today")
print("we need to put about", average_passengers_per_car, "in each car")


w = "This is the left side of ..."
e = "a string with a right side"

print("%r + %r"%(w, e))
print(w + e)
