N = int(input())

ori_x, ori_y, ori_t = 0, 0, 0
xmove, ymove = 0, 0

for _ in range(1, N + 1):
	t, x, y = map(int, input().split())
	xmove = abs(x - ori_x)
	ymove = abs(y - ori_y)
	canwalk = t - ori_t
	ori_x = x
	ori_y = y
	ori_t = t
	if canwalk >= xmove + ymove and (canwalk - xmove - ymove) % 2 == 0:
		flag = True
	else:
		flag = False
	if flag == False:
		break

if flag == True:
	print("Yes")
else:
	print("No")
