N = int(input())
a = list(map(int, input().split()))

count = [0] * 100002
for n in a:
	count[n - 1] += 1
	count[n] += 1
	count[n + 1] += 1
print(max(count))
