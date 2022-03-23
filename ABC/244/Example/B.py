x, y = 0
d = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
T = list(input())

for c in T:
	if c == "S":
		x += dx[d]
		y += dy[d]
	else:
		d += 1
		d %= 4
print(x, y)
