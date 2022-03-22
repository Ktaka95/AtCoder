N = int(input())
A = list(map(int, input().split()))

color = [False] * 8
free = 0

for a in A:
	if 1 <= a <= 399:
		color[0] = True
	elif 400 <= a <= 799:
		color[1] = True
	elif 800 <= a <= 1199:
		color[2] = True
	elif 1200 <= a <= 1599:
		color[3] = True
	elif 1600 <= a <= 1999:
		color[4] = True
	elif 2000 <= a <= 2399:
		color[5] = True
	elif 2400 <= a <= 2799:
		color[6] = True
	elif 2800 <= a <= 3199:
		color[7] = True
	else:
		free += 1
min_count = 0
for c in color:
	if c == True:
		min_count += 1
if min_count == 0:
	min_count = 1
	free -= 1
max_count = min_count + free
print(min_count, max_count)
