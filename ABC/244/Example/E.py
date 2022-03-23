MOD = 998244353

N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1

edge = [[] for _ in range(N)]

for _ in range(M):
	U, V = map(int, input().split())
	U -= 1
	V -= 1
	edge[U].append(V)
	edge[V].append(U)

dp = [[[0, 0] for _ in range(N)] for _ in range(K + 1)]

dp[0][S][0] = 1

for i in range(K):
	for v in range(N):
		for b in range(2):
			for to in edge[v]:
				dp[i + 1][to][(b + (to == X)) % 2] += dp[i][v][b]
				dp[i + 1][to][(b + (to == X)) % 2] %= MOD
print(dp[K][T][0])
