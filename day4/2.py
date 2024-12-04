grid = [line.strip() for line in open("4.in").readlines()]
tot=0

def inRange(i,j,r,c):
	# represents checking upleft, upright, downright, downleft diags
	vals = [1,1,1,1]
	if i < 3:
		vals[0]=0
		vals[3]=0
	if i > r-4:
		vals[1]=0
		vals[2]=0
	if j < 3:
		vals[0]=0
		vals[1]=0
	if j > c-4:
		vals[2]=0
		vals[3]=0
	return vals



r = len(grid)
c = len(grid[0])

checks=["MS","SM"]
# for each diag
for i in range(1,r-1):
	for j in range(1,c-1):
		# 4 diags to check, need to be sure we're only checking valid indices
		if grid[i][j]=="A":
			if (grid[i-1][j-1]+grid[i+1][j+1] in checks) and (grid[i-1][j+1]+grid[i+1][j-1] in checks): tot+=1 

print(tot)

