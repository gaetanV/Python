import subprocess
import sys
from cStringIO import StringIO
import down_rule
import re


F1 = open("down.py", "r")

C = F1.read()
C = re.sub('print[ ]*(?P<func>[A-Za-z0-9])[ ;]*$', 'raw_output(\g<func>)', C)
C = re.sub('print[ ]*[(]{1}(?P<func>[A-Za-z0-9])[)]{1}[ ;]*$', 'raw_output(\g<func>)', C)

def test(i) :
    
    print("-----seq"+i+"------")

    exec("import down_rule\n"+
         "down_rule.setSeq("+i+")\n"+
         "raw_input = down_rule.raw_input\n"+
         "raw_output = down_rule.raw_output\n"+
         C)

for i in range(len(down_rule.data)):
    test(str(i))

