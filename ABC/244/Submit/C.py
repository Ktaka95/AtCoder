N = int(input())

num = [1] * (2 * N + 2)
for i in range(1, len(num)):
	while num[i] != 1 and i != 2 * N + 1:
		i += 1
	num[i] = 0
	print(i, flush=True)
	a = int(input())
	num[a] = 0
	if max(num) == 0:
		exit()
