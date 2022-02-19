N = int(input())

max = N // 4 + N % 4
flag = False

for i in range(max + 1):
	if (N - 4 * i) % 7 == 0:
		flag = True
		break
if flag:
	print("Yes")
else:
	print("No")
