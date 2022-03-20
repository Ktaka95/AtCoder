import itertools

N, M = map(int, input().split())

adjacent_check = list([0] * (N + 1) for _ in range(N + 1))

for _ in range(M):
	a, b = map(int, input().split())
	adjacent_check[a][a] = 1
	adjacent_check[a][b] = 1
	adjacent_check[b][a] = 1
	adjacent_check[b][b] = 1

ori_root = list()
for i in range(1, N + 1):
	ori_root.append(i)

all_root = list()
for root in itertools.permutations(ori_root, len(ori_root)):
	if root[0] == 1:
		all_root.append(root)

count = 0
for i in range(len(all_root)):
	flag = True
	for j in range(N - 1):
		check1 = all_root[i][j]
		check2 = all_root[i][j + 1]
		if adjacent_check[check1][check1] < 1 or adjacent_check[check1][check2] < 1:
			flag = False
			break
	if flag:
		count += 1
print(count)
