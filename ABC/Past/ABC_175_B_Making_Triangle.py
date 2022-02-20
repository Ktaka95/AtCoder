N = int(input())
L = list(map(int, input().split()))
L_sorted = sorted(L, reverse=True)
count = 0
for i in range(N - 2):
	for j in range(i + 1, N - 1):
		for k in range(j + 1, N):
			if abs(L_sorted[j] - L_sorted[k]) < L_sorted[i] < L_sorted[j] + L_sorted[k] and L_sorted[k] < L_sorted[j] < L_sorted[i]:
				count += 1
print(count)
