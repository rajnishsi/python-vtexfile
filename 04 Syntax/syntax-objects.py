#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Egg:
    def __init__(self, kind1="friedd"):
        self.kind = kind1
        
    def whatkind(self):
        return self.kind
    
def main():
    fried = Egg()
    print(fried.whatkind())
    
if __name__ == "__main__": main()
        