import sys
from cStringIO import StringIO

data = [

    [
        [9,8,7,6,5,4,3,2],
        [0,8,7,6,5,4,3,2],  
        [0,0,7,6,5,4,3,2], 
        [0,0,0,6,5,4,3,2], 
        [0,0,0,0,5,4,3,2],
        [0,0,0,0,0,4,3,2],
        [0,0,0,0,0,0,3,2],
        [0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,1]
    ] 
]

result =  [
    [0, 1, 2, 3, 4, 5, 6, 7]
]

cmp = -1
cmp2 = 0
seq = 0
Response = []

def setSeq(nb) :
    globals()['cmp']=-1
    globals()['cmp2']=0
    globals()['seq']=nb


def raw_input() :
    globals()['cmp']+=1
    max = len(data[seq][cmp2])

  
    if cmp >= max:
        globals()['cmp2']+=1
        globals()['cmp']=0
    try:
        return data[seq][cmp2][cmp]
    except IndexError:
        exit("Out of bound")

def raw_output(message) :
    Response.append(message)
    if cmp2 + 1 == len(data[seq])-1:
        
        exit([Response,check()])

def check() :
    try:
        for i in range(len(result[seq])):
            assert Response[i] == result[seq][i]
        return 1
    except:
        return (str(Response)+" NEED TO BE EQUAL TO "+str(result[seq]))
 


