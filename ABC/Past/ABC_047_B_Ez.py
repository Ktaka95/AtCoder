W, H, N = map(int, input().split())

x_min = 0
x_max = W
y_min = 0
y_max = H

for _ in range(N):
	x, y, a = map(int, input().split())
	if a == 1:
		x_min = max(x, x_min)
	elif a == 2:
		x_max = min(x, x_max)
	elif a == 3:
		y_min = max(y, y_min)
	else:
		y_max = min(y, y_max)
width = max(0, x_max - x_min)
height = max(0, y_max - y_min)
area = width * height
print(area)
