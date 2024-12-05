d={}
f=False
tot=0
for line in open("5.in").readlines():
	if len(line)<3:
		f=True
		continue
	if f:
		valid = True
		ns = [int(x) for x in line.split(",")]
		i=0
		while i < len(ns):
			for j in range(i+1,len(ns)):
				if ns[i] not in d or (ns[i] in d and ns[j] not in d[ns[i]]):
					valid = False
					i=len(ns)
					break
			i+=1
		if valid: 
			tot += ns[len(ns)//2]
	else:
		x,y = [int(x) for x in line.split("|")]
		if x not in d:
			d[x] = []
		d[x].append(y)

print(tot)