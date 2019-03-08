#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ex17
#    Description :
#    Author :          SanYapeng
#    date：            2019-03-07
#    Change Activity:  2019-03-07:

import sys
import os

script, from_file, to_file = sys.argv

print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file, 'r').read()

print("The input file is %d bytes long" % len(in_file))


print("Does the output file exist? %r" % os.path.exists(to_file))
print("Ready hit RETURN to continue, CTRL-C to abort.")
raw_input("?")

out_file = open(to_file, 'w').write(in_file)

print("Alright, all done.")
