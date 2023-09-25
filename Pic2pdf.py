#!/bin/env python
import subprocess
import re

file_list = []
ls_cmd = "ls --color=none | grep -E '\.png$' > convert.sh ; ls --color=none | grep -E '\.jpg$' >> convert.sh ; ls --color=none | grep -E '\.jpeg' >> convert.sh "

subprocess.call(["sh","-c", ls_cmd])

with open("convert.sh", 'r') as f:
    file_list = f.readlines()

for l in range(0, len(file_list)):
    fname = re.sub(r"\.\w+\n","", file_list[l])
    new_fname = fname+".pdf"
    file_list[l] = re.sub("^", "convert ", file_list[l])
    file_list[l] = re.sub("\n", " "+new_fname+"\n", file_list[l])

with open("convert.sh", 'w') as f:
    for l in range(0, len(file_list)):
        f.write(file_list[l])


subprocess.call(["sh","convert.sh"])
subprocess.call(["rm","convert.sh"])
