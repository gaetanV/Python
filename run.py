import subprocess
import os
import json

NAME = "resolve/horse.py"
INPUT = "db/horse.json"
USER = "GIT"

F1 = open(INPUT, "r")
data = json.loads(F1.read())
F1.close()

F1 = open(NAME, "r")
C = F1.read()
F1.close()

def check(Response,Mask) :
    try:
        assert Response == Mask
        return 1
    except:
        return 0
 

def test(i) :
  
    print("-----seq"+str(i)+"------")

    A = ','.join(
        ','.join(
            str(b) for b in e
        )  
        for e in data["input"][i]
    )

    code = "import engine\n"+"engine.setSeq('"+str(A)+"')\n"+"raw_input = engine.raw_input\n"+C
    path = USER+".o"
 
    F = open(path, 'w')

    F.write(code)
    F.close()

    retcode = subprocess.check_output("py " + path, shell=True)
   
    response = retcode.strip().split('\r\n')
 
    print [
        check(response,data["output"][i]),
        response,
        data["output"][i]
    ]

    
for i in range(len(data["input"])):
    test(i)

