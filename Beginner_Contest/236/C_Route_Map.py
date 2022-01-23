N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

for i in range(N):
	if i == 0 or i == N - 1:
		print("Yes")
	elif S[i] in T:
		print("Yes")
	else:
		print("No")
