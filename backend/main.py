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
            tVar = readString.split(b)
            self.children=[]
            readString = readString[1:]
            tVar = readString.split(b)
            tVar[0] = tVar[0].split(",")
            self.size = tVar[0][0]
            self.timesCalled = tVar[0][1]
            self.name = tVar[0][2]
            self.score = tVar[0][3]
            
            if(len(tVar)>1):
                i = 1
                tVar[i] = tVar[i].split(";")
                for j in range(len(tVar[i])):
                    tVar[i][j] = tVar[i][j].split(",")
                    
                    
                    if(j==0):
                        
                        self.children.append(Exercise(readString[readString.index("{"):],1))
                    else:
                        self.children.append(Exercise(tVar[i][j],0,self.children[j-1].children))
            else: self.children = []
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
            a = []
            if(len(self.children)>1):
                self.children[1] = self.children[1].split(";")
                a = self.children[1].copy()
            self.children = []
            if(readString.find("{")):
                
                for i in range(0,len(a)):
                    if(i==0):
                        self.children.append(Exercise(readString[readString.index("{"):],1))
                    else:
                        self.children.append(Exercise(a[i].split(","),0))
                
        
with open("../data/DummyData.txt", "r") as file:
    data = file.read().rstrip()
data = data[:-1]
data = data.split("}")
a = []
for i in data:
    i = Exercise(i)
    a.append(i)
    
for i in a:
    while(len(i.children)>0):
        print(i.name, len(i.children)) 
        i = i.children[0]
    print(i.name)
