N = int(input())
N_list = list()
for _ in range(N):
	N_list.append(input())

M = int(input())
M_list = list()
for _ in range(M):
	M_list.append(input())

counter = [0] * N
for i in range(N):
	for j in range(N):
		if N_list[i] == N_list[j]:
			counter[i] += 1
	for k in range(M):
		if N_list[i] == M_list[k]:
			counter[i] -= 1
if max(counter) > 0:
	print(max(counter))
else:
	print(0)
