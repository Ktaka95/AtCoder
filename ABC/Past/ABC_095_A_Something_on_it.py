S = list(input())
cnt = 0

for i in range(len(S)):
	if S[i] == 'o':
		cnt += 1
print(700 + cnt * 100)
