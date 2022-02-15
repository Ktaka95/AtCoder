N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
	for i in range(N):
		if A[i] % 2 == 0:
			A[i] = A[i] / 2
		else:
			break
	if i == N - 1:
		cnt += 1
	else:
		break
print(cnt)
