#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = [1,2,3]
    x.append(5)
    x.insert(0,0)
    x.insert(4,4)
    print(type(x), x[0:5])
    
    
if __name__ == "__main__": main()
