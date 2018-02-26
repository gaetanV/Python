import subprocess
import os
import json

LANG = "c"
NAME = "resolve/horse.exe"

INPUT = "db/horse.json"
USER = "GIT"

F1 = open(INPUT, "r")
data = json.loads(F1.read())
F1.close()

def runShell():
    for i in range(len(data["input"])):
        if LANG == 'py':
            CMD = "py " + NAME
        else:
            CMD = NAME
            
        sp = subprocess.Popen(
            CMD,            
            stdin = subprocess.PIPE, 
            stdout = subprocess.PIPE,
        )
        A = '\n'.join(
            '\n'.join(
                str(b) for b in e
            )  
            for e in data["input"][i]
        )

        response = sp.communicate(input=A)[0].decode().strip().split('\r\n')
        print [
            check(response,data["output"][i]),
            response,
            data["output"][i]
        ]


def runInject():
    
    F1 = open(NAME, "r")
    C = F1.read()
    F1.close()

    for i in range(len(data["input"])):
        print("-----seq"+str(i)+"------")

        A = ','.join(
            ','.join(
                str(b) for b in e
            )  
            for e in data["input"][i]
        )

        code = "import engine\n"+"engine.setSeq('"+str(A)+"')\n"+"raw_input = engine.raw_input\n"+"open = engine.open\n"+C
        path = USER+".o"
    
        F = open(path, 'w')

        F.write(code)
        F.close()
        try:
            retcode = subprocess.check_output("py " + path, shell=True)
            response = retcode.strip().split('\r\n')
            print [
                check(response,data["output"][i]),
                response,
                data["output"][i]
            ]
        except subprocess.CalledProcessError as e:

            def illegal():
                print "Error illegal native action\n"
            def hack():
                print "Don't try to hack\n"
            {
                2:hack,
                3:illegal
            }[e.returncode]()

def check(Response,Mask) :
    try:
        assert Response == Mask
        return 1
    except:
        return 0
 


runShell()