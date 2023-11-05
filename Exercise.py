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
        #This piece defines the root node.
        if(ind==-1):
            tVar = readString.split(b)
            self.children=[]
            readString = readString[1:]
            tVar = readString.split(b)
            #Define the root's own aspects
            tVar[0] = tVar[0].split(",")
            self.size = tVar[0][0]
            self.timesCalled = int(tVar[0][1])
            self.name = tVar[0][2]
            self.score = float(tVar[0][3])
           
            #Define the root's children
            if(len(tVar)>1):
                #i = 1 because this was a loop and I'm too lazy to change it.
                i = 1
                tVar[i] = tVar[i].split(";")
                #Loop through the layer of nodes adjacent to the
                #root and initialize them.
                for j in range(len(tVar[i])):
                    tVar[i][j] = tVar[i][j].split(",")
                    
                    
                    if(j==0):
                        #In this call, all the children for the
                        #layer beneath this one (they would be
                        #found in tVar[2] here) are initialized
                        #before the rest of the children in tVar[1] are.
                        #This is a depth-first recursion.
                        self.children.append(Exercise(readString[readString.index("{"):],1))
                    else:
                        self.children.append(Exercise(tVar[i][j],0,self.children[j-1].children))
            #likely redundant but not worth removing and finding out.
            else: self.children = []
        elif(ind==0):
            self.name = readString[0]
            self.children = []
            self.score = float(readString[1])
            #The list of children has already been made for us; it is in
            #The first node of this layer. It is passed in to us from the
            #caller.
            for i in range(len(lst)):
                self.children.append(lst[i])
            
        else:
            #This is the branch of the function that is called when
            #Initializing the first node on a new layer. It defines its
            #own first child (in children[0]--the use of self.children)
            #before the initialization of a is clunky and ought ot be 
            #replaced with more time. Once it has the full list of its
            #grand children from children[0], it can use that list to 
            #initialize the rest of its children.
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



    def toSendString(self, node):
        s = node.name + ':' + str(node.score) + ';'
        s += self.getChildString(node)

        #print(s)
        if(len(node.children) != 0):
            #print('next: ', node.children[0].name, '\n')
            return s + self.toSendString(node.children[0])
        return s

    def getChildString(self, node):
        s = ''
        for c in node.children:
            s += c.name + ':' + str(c.score) + ';'
        return s

    def toFormatString():
        #print all of this thing's info
        a = "{" + string(self.timesCalled) + "," + \
            string(self.size) + "," + self.name + \
                "," + string(self.score)
        if(len(a.children)>0):
            a = a + "{"
        #print all of its childrens' info
            for i in range(len(self.children)):
                a = a + self.children[i].name + "," +\
                    self.children[i].score
                if(i+1<len(self.children)):
                    a = a + ";"
                else: a = a + "{"
            a += self.children[0].toFormatStringChild()
        a = a + "}"
        return a
        
    def toFormatStringChild():
        if(len(a.children)>0):
            print("a")
        #print all of this thing's childrens' info
        #call this for this things' children[]
        


#With correct input this function should always work.

#Don't mess with it.
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


#Tree traversal. Returns a string with the name of an exercise. 
def select(ex):
    ex.timesCalled+=1
    random.seed(a=None,version=2)
    st = ex.name
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
            st = ",".join([st,ex.name])
    print(st)
    return st

def update(ex, exercises):
    root = None
    ex = ex.split(":")
    for i in range(len(ex)):
       ex[i] = ex[i].split(",")
    for i in exercises:
        if(ex[0][0]==i.name):
            root = i
            break
    if not root:
        return
    arr = []
    root.score *=5
    root.score +=int(ex[0][1])
    root.score /=6
    prevRoot = root
    for i in range(1, len(ex)):
        j = 0
        while(j < len(root.children)):
            if(root.children[j] == ex[i][0]):
                root = root.children[j]
                arr.append(j)
                break
            j+=1
        if(root == prevRoot):
            return
        prevRoot = root
        root.score *=5
        root.score +=int(ex[i][1])
        root.score /=6
    
            
        

'''
a = parse("../data/DummyData.txt")
for i in range(2):
    select(a[0])
select(a[1])
select(a[2])
for i in range(200):
    update("Jump,0:Full Hop,0:Fast Fall,0:Dair,0:Forward 0.5,0", a)
print(a[0].score)
    
'''
        
        
