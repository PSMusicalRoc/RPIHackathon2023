# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:15:34 2023

@author: TJ
"""
import fileinput
import numpy as n
class Exercise:
    #Recursively creates all objects readable from the string.
    

    def __init__(self, readString, ind=-1, lst = []):
        b = "{"
        if(ind==-1):
            readString = readString[1:]
            self.children = readString.split(b)
            self.children[0] = self.children[0].split(",")
            self.size = self.children[0][0]
            self.timesCalled = self.children[0][1]
            self.name = self.children[0][2]
            self.score = self.children[0][3]
            if(len(self.children)>1):
                i = 1;
                self.children[i] = self.children[i].split(";")
                for j in range(len(self.children[i])):
                    self.children[i][j] = self.children[i][j].split(",")
                  
                    if(j==0):
                        self.children[i-1] = Exercise(readString[readString.index("{"):],1)
                    else:
                        self.children[i-1] = Exercise(self.children[i][j],0,self.children[i-1].children)
        elif(ind==0):
            self.name = readString[0]
            self.children = []
            self.score = readString[1]
            for i in range(len(lst)):
                self.children.append( lst[i])
            
        else:
            readString = readString[1:]
            self.children = readString.split("{")
            self.children[0] = self.children[0].split(";")
            self.children[0][0] = self.children[0][0].split(",")
            self.name = self.children[0][0][0]
            self.score = self.children[0][0][1]
            if(len(self.children)>1):
                self.children[1] = self.children[1].split(";")
                a = self.children[1].copy()
                for i in range(0,len(a)):
                    if(i==0):
                        self.children[i] = Exercise(readString[readString.index("{"):],1)
                    else:
                        self.children[i] = Exercise(a[i].split(","),0)
                
        
a = Exercise("{4,1000,Jump,10{Full hop,10;Short hop,10{Fast fall,10;,10")
b = Exercise("{1, 1, Roll, 10")
