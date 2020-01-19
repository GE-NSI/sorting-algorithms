


def Greatest():
    t = [3, 5, 1, 8, 4, 2 , 9, 8, 158]
    l = len(t)-1
    G = t[0]
    for i in range(l):
        i = i+1
        if G < t[i]:
            G = t[i]
    print (G)

#GRUAU Elyan, IG4
def square():
    t=[1, 2, 3, 4, 5, 6 , 7, 8, 9]
    i = 0
    l = len(t)
    for i in range(l):
        t[i]= t[i]*t[i]
        i = i+1
    return t

def newsquare():
    Tbegin = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
    Tend = []
    i = 0
    l = len(Tbegin)
    for i in range(l):
        Tend.append(Tbegin[i]*Tbegin[i])

        i = i+1
    return Tbegin, Tend

def belong (n,t):
        i=0
        while i<= len(t):
            if n == t[i]
                return True
            i=i+1
            return False
def Somme():
res=t[0]
for i in range (i,len(t)):
    res=res+t[i]
    return res

def greatest-in(t)
res=t[0]
for element in t:
    if element >res:
        res=element
    return res

def mglen(t):
    cpt=0
    for element in t:
        cpt = cpt+1
    return cpt

def map-double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def smallestin(t,i,j):
    for indice in range (i,j+1):
        if t[indice]<res:
            res =t[indice]
        return (res)

def swap (t,j,j):
    saume=t[i]
    t[i]=t[j]
    t[j]=saume

def remove (t,i):
    res=[0]*(len(t)-1)
    for j in range
        if j< i
            res[j]=t[j]
        if j>i
            res [j-1]=t[j]
    return, (t,j)

def mySelectionin(t):
    res=[0]*len(t)
    for i in range (len(t)):
        j=index of smallestin(t)
        res=[j]=t[j]
        remove (t,j)



