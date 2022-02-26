a1 = 0
b_list = list(map(int, input().split()))
flag = True
for _ in range(2):
	a_list = list(map(int, input().split()))
	standard = a_list[0] - b_list[0]
	for i in range(1, 3):
		if a_list[i] - b_list[i] != standard:
			flag = False
			break
if flag:
	print("Yes")
else:
	print("No")
