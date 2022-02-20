N = int(input())
a = list(map(int, input().split()))
ball = list()
dup_count = 1

for i in range(N):
	ball.append(a[i])
	if i >= 1 and a[i] == ball[-2]:
		dup_count += 1
		if dup_count == a[i]:
			del ball[-a[i]:]
			dup_count = 1
			j = 1
	print(ball, len(ball), dup_count)
