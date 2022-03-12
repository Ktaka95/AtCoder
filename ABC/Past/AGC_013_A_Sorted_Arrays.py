N = int(input())
A = list(map(int, input().split()))

arry_num = 1
i = 0
while i <= N - 2:
	if A[i] == A[i + 1]:
		while i <= N - 2 and A[i] == A[i + 1]:
			i += 1
	elif A[i] < A[i + 1]:
		while i <= N - 2 and A[i] <= A[i + 1]:
			i += 1
		if i != N - 1:
			arry_num += 1
		if i <= N - 2:
			i += 1
	else:
		while i <= N - 2 and A[i] >= A[i + 1]:
			i += 1
		if i != N - 1:
			arry_num += 1
		if i <= N - 2:
			i += 1
print(arry_num)
