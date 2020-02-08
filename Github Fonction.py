#GRUAU Elyan, IG4
# Les fonctions T(...) sont des fonctions test.
# [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX] Fonctions Primitives [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#1 --> belong <---------------------------------------------------------------------------->
def belong(n,t): #ok
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False

def Tbelong():
    n=10
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False
#2  --> greatestin <---------------------------------------------------------------------------->
def greatestin(t):
    res=t[0]
    for element in t:
        if element > res:
            res=element

def Tgreatestin():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    res=t[0]
    for element in t:
        if element > res:
            res=element
#3  --> mysomme <---------------------------------------------------------------------------->
def mysomme(t):
    res=t[0]
    for i in range(i,len(t)):
        res=res+t[i]
    return res

def Tmysomme(t):
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    res=t[0]
    for i in range(i,len(t)):
        res=res+t[i]
    return res
#4  --> mylen<---------------------------------------------------------------------------->
def mylen(t):
    cpt=0
    for element in t:
        cpt = cpt+1
    return cpt

def Tmylen():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    cpt=0
    for element in t:
        cpt = cpt+1
    return cpt
#5  --> swap <---------------------------------------------------------------------------->
def swap (t,i,j):
    saume=t[i]
    t[i]=t[j]
    t[j]=saume

def Tswap():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    saume=t[i]
    t[i]=t[j]
    t[j]=saume
#6  --> remove <---------------------------------------------------------------------------->
def remove(t,i):
    res=[0]*(len(t)-1)
    for j in range:
        if j< i:
            res[j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return (t,j)

def Tremove():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    res=[0]*(len(t)-1)
    for j in range:
        if j< i:
            res[j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return (t,j)
#7 --> mydouble <---------------------------------------------------------------------------->
def mapdouble(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def Tmapdouble():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res
#8 --> square <---------------------------------------------------------------------------->
def square(t):
    for i in range(len(t)):
        t[i]= t[i]*t[i]
    return t

def Tsquare():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
#9 --> mysort <---------------------------------------------------------------------------->
def mysort(t):
    for j in range(l, len(t)):
        T=t[j]
        i =j- 1
        while i>=0 and t[i]>T:
            t[i+1]=t[i]
            i=i-1
        t[i+1]= T
    return t

def Tmysort():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    for j in range(l, len(t)):
        T=t[j]
        i =j- 1
        while i>=0 and t[i]>T:
            t[i+1]=t[i]
            i=i-1
        t[i+1]= T
    return t
#10 --> smallestin <---------------------------------------------------------------------------->
def smallestin(t,i,j):
    for indice in range (i,j+1):
        if t[indice]<res:
            res =t[indice]
        return (res)

def Tsmallestin():
    t=[1,2,3,4,5,6,7,8,9,10,2048,512]
    for indice in range (i,j+1):
        if t[indice]<res:
            res =t[indice]
        return (res)

# [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX] Fonctions Tributaires [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]

#1 --> insert <---------------------------------------------------------------------------->
def insert(t,i):
    for current_index in range(i-1,-1,-1):
        if t[current_index] > t[current_index+1]:
            swap(t,current_index,current_index+1)
        else:
            break

#2 --> myselectionin<---------------------------------------------------------------------------->
def myselectionin(t):
    res=[0]*len(t)
    for i in range (len(t)):
        j= index-of-smallestin(t)
        res=[j]=t[j]
        remove (t,j)

#3 --> insertion_in_place<---------------------------------------------------------------------------->
def insertioninplace(t):
    for index in range(len(t)):
        s = indexofthesmallest
    if s > index:
     swap(t,index,s)
    return null

#4 --> insertion_sort_in_place<---------------------------------------------------------------------------->
def insertion_sort_in_place(t):
        for index in range(i,len(t)):
            insert(t,index)
