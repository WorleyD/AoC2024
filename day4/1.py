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
# for each row
for line in grid:
	# horizontal occurrences
	tot+=line.count("XMAS") + line.count("SAMX")


# for each col
for i in range(c):
	col= "".join([l[i] for l in grid])
	# vertical occurrences
	tot+=col.count("XMAS") + col.count("SAMX")

# for each diag
for i in range(r):
	for j in range(c):
		# 4 diags to check, need to be sure we're only checking valid indices
		if grid[i][j]=="X":
			checks=inRange(i,j,r,c)
			# check upLeft
			if checks[0]:
				if grid[i-1][j-1] == "M" and grid[i-2][j-2] == "A" and grid[i-3][j-3]=="S": tot+=1
			if checks[1]:
				if grid[i+1][j-1]=="M" and grid[i+2][j-2]=="A" and grid[i+3][j-3]=="S": tot+=1
			if checks[2]:
				if grid[i+1][j+1]=="M" and grid[i+2][j+2]=="A" and grid[i+3][j+3]=="S": tot+=1
			if checks[3]:
				if grid[i-1][j+1]=="M" and grid[i-2][j+2]=="A" and grid[i-3][j+3]=="S": tot+=1

print(tot)

