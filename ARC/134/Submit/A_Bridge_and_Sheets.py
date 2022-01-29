N, L, W = map(int, input().split())
an = list(map(int, input().split()))

bridge = [0] * (L + 1)
cnt = 0
for _ in range(N):
	covered = [0] * (L + 1)
	for i in range(L + 1):
		covered[i] = i
	covered = covered[an[_]:an[_] + W + 1]
	for c in covered:
		bridge[c] += 1
for j in range(L):
	if bridge[j] == 0:
		cnt += 1
		k = 0
		while k < W and j < L + 1:
			bridge[j] += 1
			j += 1
			k += 1
print(cnt)
