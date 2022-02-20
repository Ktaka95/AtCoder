a, b = map(int, input().split())
flag = False

if a == 1:
	if b == 10:
		flag = True
if a == 10:
	if b == 1:
		flag = True
else:
	if abs(a - b) == 1:
		flag = True
if flag:
	print("Yes")
else:
	print("No")
