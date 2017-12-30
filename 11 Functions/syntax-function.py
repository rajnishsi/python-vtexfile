#!/usr/bin/python3
# jumptable.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    rangefunc()
    rangefunc(3)
    

def rangefunc(a=1):
    for r in range(a,10):
        print(r, end=' ')
    print()
        
if __name__=="__main__" : main()
        