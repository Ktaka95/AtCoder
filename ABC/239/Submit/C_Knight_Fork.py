x_1, y_1, x_2, y_2 = map(int, input().split())

p1 = [x_1, y_1]
p2 = [x_2, y_2]

p1_1 = [x_1 + 5, y_1]
p1_2 = [x_1 + 2, y_1 + 1]
p1_3 = [x_1 + 1, y_1 + 2]
p1_4 = [x_1 - 5, y_1]
p1_5 = [x_1 - 2, y_1 + 1]
p1_6 = [x_1 - 1, y_1 + 2]
p1_7 = [x_1 + 2, y_1 - 1]
p1_8 = [x_1 + 1, y_1 - 2]
p1_9 = [x_1 - 2, y_1 - 1]
p1_10 = [x_1 -1, y_1 - 2]

p2_1 = [x_2 + 5, y_2]
p2_2 = [x_2 + 2, y_2 + 1]
p2_3 = [x_2 + 1, y_2 + 2]
p2_4 = [x_2 - 5, y_2]
p2_5 = [x_2 - 2, y_2 + 1]
p2_6 = [x_2 - 1, y_2 + 2]
p2_7 = [x_2 + 2, y_2 - 1]
p2_8 = [x_2 + 1, y_2 - 2]
p2_9 = [x_2 - 2, y_2 - 1]
p2_10 = [x_2 -1, y_2 - 2]

p1list = [p1_1, p1_2, p1_3, p1_4, p1_5, p1_6, p1_7, p1_8, p1_9, p1_10]

p2list = [p2_1, p2_2, p2_3, p2_4, p2_5, p2_6, p2_7, p2_8, p2_9, p2_10]

flag = False
for i in range(10):
	for j in range(10):
		if p1list[i] == p2list[j]:
			flag = True
			break
if flag:
	print("Yes")
else:
	print("No")
