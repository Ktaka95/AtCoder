N = int(input())
S = input()
A = [0]
k = 0
for i in range(N):
	if S[i] == 'L':
		A.insert(k, i + 1)
	else:
		A.insert(k + 1, i + 1)
		k += 1
print(*A)
