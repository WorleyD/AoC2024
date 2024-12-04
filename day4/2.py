grid = [line.strip() for line in open("4.in").readlines()]
tot=0
r = len(grid)
c = len(grid[0])
checks=["MS","SM"]
# for each diag
for i in range(1,r-1):
	for j in range(1,c-1):
		if grid[i][j]=="A":
			if (grid[i-1][j-1]+grid[i+1][j+1] in checks) and (grid[i-1][j+1]+grid[i+1][j-1] in checks): tot+=1 

print(tot)

