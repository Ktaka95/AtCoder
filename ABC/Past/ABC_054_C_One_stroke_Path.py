N, M = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
	dp[i][0] = 1
for _ in range(M):
	a, b = map(int, input().split())
	dp[a][b] = 1
	dp[b][a] = 1
	print(dp)


