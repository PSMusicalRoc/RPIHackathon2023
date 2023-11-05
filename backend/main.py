# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:15:34 2023

@author: TJ
"""
import fileinput
import numpy as n
import random
class Exercise:
    #Recursively creates all objects readable from the string.
    

    def __init__(self, readString, ind=-1, lst = []):
        b = "{"
        self.lastPath = -1
        self.lastMult = .5
        #This piece 
        if(ind==-1):
            tVar = readString.split(b)
            self.children=[]
            readString = readString[1:]
            tVar = readString.split(b)
            tVar[0] = tVar[0].split(",")
            self.size = tVar[0][0]
            self.timesCalled = int(tVar[0][1])
            self.name = tVar[0][2]
            self.score = float(tVar[0][3])
           
            
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
            self.score = float(readString[1])
            for i in range(len(lst)):
                self.children.append(lst[i])
            
        else:
            readString = readString[1:]
            
            self.children = readString.split("{")
            self.children[0] = self.children[0].split(";")
            self.children[0][0] = self.children[0][0].split(",")
            self.name = self.children[0][0][0]
            self.score = float(self.children[0][0][1])
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
                        self.children.append(Exercise(a[i].split(","),0, self.children[i-1].children))
                
def parse(filename):      
    with open(filename, "r") as file:
        data = file.read().rstrip()
    data = data[:-1]
    data = data.split("}")
    a = []
    for i in data:
        i = Exercise(i)
        a.append(i)
        
    for i in a:
        while(len(i.children)>0):
            i = i.children[0]
    return a

def select(ex):
    ex.timesCalled+=1
    random.seed(a=None,version=2)
    st = ex.name + ":"
    while(len(ex.children)>0):
        rand = random.random()
        while(rand<=0):
            rand = random.random()
        a = 0
        for i in range(len(ex.children)):
            temp = 1
            if(i == ex.lastPath):
                temp = ex.lastMult
            a+=(temp*(1.01-ex.children[i].score))
        rand *=a
        i = 0
        t = 0.0
        while(rand > t):
            temp = 1
            if(i == ex.lastPath):
                temp = ex.lastMult
            t+=(temp*(1.01-ex.children[i].score))
            i+=1
        i-=1
        if(i!=ex.lastPath):    
            ex.lastPath = i
            ex.lastMult = 0.5
        else:
            ex.lastMult*=.5
        ex = ex.children[i]
        if(ex.name):
            st = " ".join([st,ex.name])
    print(st)
    return st

a = parse("../data/DummyData.txt")
for i in range(200):
    select(a[0])
select(a[1])
select(a[2])
    
        
        
        
