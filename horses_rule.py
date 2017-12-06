data =  [
    [3,5,8,9],
    [10,5,15,17,3,8,11,28,6,55,7]
]

result =  [
    1,
    1
]

cmp = -1
seq = 0
def setSeq(nb) :
    globals()['cmp']=-1
    globals()['seq']=nb

def raw_input() :
    globals()['cmp']+=1
    if data[seq][cmp] :
      return data[seq][cmp]
    print("Out of bound")
    exit

def check(response) :
    try:
        assert response == result[seq]
        print(str(response)+" IS EQUAL TO "+str(result[seq]))
    except:
        print(str(response)+" NEED TO BE EQUAL TO "+str(result[seq]))




