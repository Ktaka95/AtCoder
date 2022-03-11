N = int(input())
x_y_h = [list(map(int, input().split())) for _ in range(N)]

for x, y, h in x_y_h:
	if h != 0:
		tmp_x, tmp_y, tmp_h = x, y, h
		break
for cx in range(101):
	for cy in range(101):
		flag = True
		H = abs(tmp_x - cx) + abs(tmp_y - cy) + tmp_h
		for x, y, h in x_y_h:
			calc_H = max(H - abs(x - cx) - abs(y - cy), 0)
			if calc_H != h:
				flag = False
				break
		if flag:
			print(cx, cy, H)
