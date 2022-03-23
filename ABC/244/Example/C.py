N = int(input())

used = [False] * (2 * N + 2)

for _ in range(N + 1):
	num = 1
	while used[num]:
		num += 1
	print(num)
	used[num] = True
	x = int(input())
	used[x] = True
