N, K = map(int, input().split())
A = list(map(int, input().split()))

A_key_count = {}
for n in range(N):
	if A[n] not in A_key_count:
		A_key_count[A[n]] = 0
	A_key_count[A[n]] += 1

change = len(A_key_count) - K
if change <= 0:
	print(0)
else:
	count = 0
	A_count_sorted = sorted(A_key_count.values())
	for i in range(change):
		count += A_count_sorted[i]
	print(count)
