#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
try:
    fh = open("lines.txt")
    for r in fh.readlines():
        print(r, end='')
    
except  IOError as e:
    print("something bad happened ({})". format(e))
    
print("continue printing")