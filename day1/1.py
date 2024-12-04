l1,l2=[],[]
for line in open("1.in","r"):
	l=line.split()
	l1.append(int(l[0]))
	l2.append(int(l[1]))

l1.sort()
l2.sort()
print(sum([abs(l1[i]-l2[i]) for i in range(len(l1))]))