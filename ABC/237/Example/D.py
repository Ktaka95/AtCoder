from collections import deque

dq = deque()

N = int(input())
S = input()

dq.append(N)

for i in range(N - 1, -1, -1):
	if S[i] == 'L':
		dq.append(i)
	else:
		dq.appendleft(i)
print(*dq)
