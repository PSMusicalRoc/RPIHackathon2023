# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:15:34 2023

@author: TJ
"""


import random
class Exercise:
    #Recursively creates all objects readable from the string.
    

    def __init__(self, readString, ind=-1, lst = [], ch = "{"):
        self.lastPath = -1
        self.lastMult = .5
        #This piece defines the root node.
        if(ch==":"):
            if(ind==-1):
                tVar = readString.split(ch)
                for i in range(len(tVar)):
                    tVar[i] = tVar[i].split(";")
                self.children = []
                self.name = tVar[0][0]
                self.score = 0.2
                self.timesCalled = 0
                if(len(tVar)>1):
                    self.size =len(tVar[1])
                    for i in range(len(tVar[1])):
                        if(i==0):
                            self.children.append(Exercise(readString[readString.index(ch)+1:],0,ch=":"))
                            self.size *= self.children[0].size
                        else:
                            self.children.append(Exercise(tVar[1][i],1,self.children[0].children,":"))
            elif (ind==0):
                tVar = readString.split(ch)
                tVar[0] = tVar[0].split(";")
                self.name = tVar[0][0]
                self.score = 0.2
                self.size = 1
                self.children = []
                if(len(tVar)>1):
                    tVar[1] = tVar[1].split(";")
                    self.size *= len(tVar[1])
                    for i in range(len(tVar[1])):
                        if(i==0):
                            self.children.append(Exercise(readString[readString.index(ch)+1:],0,ch=":"))
                            self.size *= self.children[0].size
                        else: 
                            self.children.append(Exercise(tVar[1][i],1,self.children[0].children,ch=":"))
            else:
                self.name = readString
                self.score = 0.2
                self.children = lst
            return
        if(ind==-1):
            tVar = readString.split(ch)
            self.children=[]
            if(ch=="{"):
                readString = readString[1:]
            tVar = readString.split(ch)
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


#Get in format Action:layer1(separated by semicolons):layer2:etc......(6 dots delimeter)Action:layer1:layer2


    def toSendString(self, node):
        s = node.name + ';' + str(node.score) + ';:'
        s += self.getChildString(node)

        #print(s)
        if(len(node.children) != 0):
            #print('next: ', node.children[0].name, '\n')
            return s + self.toSendString(node.children[-1])
        return s

    def getChildString(self, node):
        s = ''
        if(len(node.children)>1):
            for c in node.children[:-1]:
                s += c.name + ';' + str(c.score) + ';'
        return s

    def toFormatString(self):
        #print all of this thing's info
        a = "{" + str(self.size) + "," + \
            str(self.timesCalled) + "," + self.name + \
                "," + str(self.score)
        if(len(self.children)>0):
            a = a + "{"
        #print all of its childrens' info
            for i in range(len(self.children)):
                a = a + self.children[i].name + "," +\
                    str(self.children[i].score)
                if(i+1<len(self.children)):
                    a = a + ";"
                else: a = a + "{"
            a += self.children[0].toFormatStringChild()
        a = a + "}"
        return a
        
    def toFormatStringChild(self):
        a = ""
        if(len(self.children)>0):
            for i in range(len(self.children)):
                a = a + self.children[i].name + \
                    "," + str(self.children[i].score)
                if(i+1<len(self.children)):
                    a = a + ";"
                else:
                    if(len(self.children[0].children)>0):
                        a = a + "{"
            a = a + self.children[0].toFormatStringChild()
        return a
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


#Loops through each exercise, calls toString, and writes to file.
def write(filename, exercises):
    a = ""
    for i in exercises:
        a += i.toFormatString()
    with open(filename, "w") as file:
        file.write(a)
        

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
    return st

#Updates scores along a specified path in the tree.
def scoring(exercises, ex, n):
    root = None
    ex = ex.split(":")
    for i in exercises:
        if(ex[0]==i.name):
            root = i
            break
    if not root:
        return
    arr = []
    root.score *=5
    root.score +=n
    root.score /=6
    if(root.score <=.01):
        root.score = .01
    prevRoot = root
    for i in range(1, len(ex)):
        j = 0
        while(j < len(root.children)):
            if(root.children[j].name == ex[i]):
                root = root.children[j]
                arr.append(j)
                break
            j+=1
        if(root == prevRoot):
            return
        prevRoot = root
        root.score *=5
        root.score +=n
        root.score /=6
        if(root.score <=.01):
            root.score = .01
            

            
def addExercise(exercises, a):
    exercises.append(Exercise(a,ch = ":"))
    
def getExercises(exercises, a):
    tot = 0
    arr = []
    lasti = -1
    discourage = .5
    for i in range(a):
        tot = 0
        for j in range(len(exercises)):
            x = 1
            if(j == lasti):
                x = discourage
            tot += x*(1.1-exercises[j].score)
        r = random.random()
        r *=tot
        b = 0
        j = 0
        while(b < r):
            x = 1
            if(j==lasti):
                x = .5
            b+=x*(1.1-exercises[j].score)
            j+=1
        j-=1
        if(lasti==j):
            discourage *=.5
        else:
            discourage = .5
        lasti = j
        arr.append(select(exercises[j]))
    return arr

def remove(exercises, name):
    for i in range(len(exercises)):
        if(exercises[i].name==name):
            exercises.pop(i)
            return


"""   
a = parse("t.txt")
for i in range(2):
    select(a[0])
select(a[1])
select(a[2])
for i in range(15):
    scoring(a,"Jump:Full Hop:Fast Fall:Dair:Forward 0.5", .5)
print(a[0].score)
print(a[0].toFormatString())
print(a[0].toSendString(a[0]))
write("t.txt",a)

addExercise(a, "Jump:Short Hop;Full Hop;:Fastfall:bo:a;Test2:Something:Nothing;Here;......")
print(a[3].children[0].name)
getExercises(a, 8)
remove(a, "Jump")
print(a[0].name)
"""


        
