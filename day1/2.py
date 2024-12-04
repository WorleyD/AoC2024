l1,l2=[],{}
for line in open("1.in","r"):
	l=[int(x) for x in line.split()]
	l1.append(l[0])
	if l[1] in l2:
		l2[l[1]]+=1
	else:
		l2[l[1]]=1

s = 0
for l in l1:
	if l in l2:
		s+=l*l2[l]
print(s)