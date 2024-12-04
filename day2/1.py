def safe(r):
	diffs= [int(r[i]) - int(r[i-1]) for i in range(1, len(r))]
	return not(any([d<=0 for d in diffs]) and any(d >= 0 for d in diffs)) and 1 <= abs(min(diffs)) <= 3 and 1<=abs(max(diffs))<=3

t=0
for report in open("2.in"):
	if safe(report.split()):t+=1
print(t)
