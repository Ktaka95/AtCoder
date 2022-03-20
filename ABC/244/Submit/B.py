N = int(input())
T = list(input())

point = [0] * 2
angle = "E"

for i in range(N):
	if T[i] == 'S':
		if angle == "E":
			point[0] += 1
		elif angle == "S":
			point[1] -= 1
		elif angle == "W":
			point[0] -= 1
		else:
			point[1] += 1
	else:
		if angle == "E":
			angle = "S"
		elif angle == "S":
			angle = "W"
		elif angle == "W":
			angle = "N"
		else:
			angle = "E"
print(*point)
