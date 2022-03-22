N, K = map(int, input().split())

arry = [0] * (100001)

for i in range(N):
	a, b = map(int, input().split())
	arry[a] += b
count = 0
for i in range(len(arry)):
	count += arry[i]
	if count >= K:
		print(i)
		break
