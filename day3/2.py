import re
from operator import mul
from functools import reduce
matches = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)",open("3.in").read())
print(matches)
f=True
s=0
for m in matches:
	if m == "do()":
		f=True
	elif m =="don't()":
		f=False
	else:
		if f:
			dig=m[4:-1].split(",")
			s+=int(dig[0])*int(dig[1])
print(s)
