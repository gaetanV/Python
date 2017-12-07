import subprocess
import sys
from cStringIO import StringIO
import horses_rule

F1 = open("horse.py", "r")
C = F1.read()

def test(i) :
    print("-----seq"+i+"------")
    o = sys.stdout
    r = sys.stdout = StringIO()

    exec("import horses_rule\n"+
         "horses_rule.setSeq("+i+")\n"+
         "raw_input = horses_rule.raw_input\n"+
         C)

    sys.stdout = o
    res = r.getvalue().strip()
    print(res)
    horses_rule.check(res)

for i in range(len(horses_rule.data)):
    test(str(i))

