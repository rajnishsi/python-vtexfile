#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = dict(
       key1 = 1, key2 = 2, key3 = 'value3'
        )
    
    for k in d.keys():
        print(k, d[k])
   
if __name__ == "__main__": main()