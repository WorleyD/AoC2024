import re
from operator import mul
from functools import reduce
print(sum([reduce(mul, [int(i) for i in match[4:-1].split(",")],1) for match in re.findall("mul\([0-9]+,[0-9]+\)",open("3.in").read())]))
