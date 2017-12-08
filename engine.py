pointer=-1
lock=0
def setSeq(data) :
    if lock == 1:
        exit(0)
    globals()['pointer']=-1
    globals()['data']=data.split(',')
    globals()['lock']=1

def raw_input() :
    globals()['pointer']+=1
    try:
       return data[pointer]
    except IndexError:
       exit(0)
