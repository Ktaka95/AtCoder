from collections import deque

sx, sy, tx, ty = map(int, input().split())

x_distance = tx - sx
y_distance = ty - sy
root = deque()

for _ in range(x_distance):
	root.append("R")
for _ in range(y_distance):
	root.append("U")
for _ in range(x_distance):
	root.append("L")
for _ in range(y_distance):
	root.append("D")
root.append("D")
for _ in range(x_distance + 1):
	root.append("R")
for _ in range(y_distance + 1):
	root.append("U")
root.append("LU")
for _ in range(x_distance + 1):
	root.append("L")
for _ in range(y_distance + 1):
	root.append("D")
root.append("R")
print(*root, sep='')
