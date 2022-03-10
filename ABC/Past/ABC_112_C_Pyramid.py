N = int(input())
x_y_h = [list(map(int, input().split())) for _ in range(N)]

for X in range(101):
	for Y in range(101):
		for i in range(N):
			H = x_y_h[i][2] + abs(x_y_h[i][0] - X) + abs(x_y_h[i][1] - Y)
			for x, y, h in x_y_h:
				calc = max(H - abs(x - X) - abs(y - Y), 0)
				if calc != H:
					break
			print(X, Y, H)
