def safe(r):
	diffs= [int(r[i]) - int(r[i-1]) for i in range(1, len(r))]
	return not(any([d<=0 for d in diffs]) and any(d >= 0 for d in diffs)) and 1 <= abs(min(diffs)) <= 3 and 1<=abs(max(diffs))<=3

def safeButOne(r):
	return any([safe(r[0:i] + r[i+1:]) for i in range(len(r))])
	
t=0
for report in open("2.in"):
	if safeButOne([x for x in report.split()]):t+=1
print(t)
