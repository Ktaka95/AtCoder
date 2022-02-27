Q = int(input())
A = list()
for i in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		A.append(query[1])
		A = sorted(A)
	elif query[0] == 2:
		x = query[1]
		k = query[2]
		A_min = [i for i in A if i <= x]
		if len(A_min) < k:
			print(-1)
		else:
			print(A_min[-k])
	else:
		x = query[1]
		k = query[2]
		A_max = [i for i in A if i >= x]
		if len(A_max) < k:
			print(-1)
		else:
			print(A_max[k - 1])
