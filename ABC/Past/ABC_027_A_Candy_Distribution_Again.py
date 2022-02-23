N, x = map(int, input().split())
a = list(map(int, input().split()))

a_index = list()
for i in range(1, N + 1):
	a_index.append(i)
a_with_index = list(zip(a, a_index))
a_sorted = sorted(a_with_index)
count = 0
i = 0
while x > 0 and i < N - 1:
	x -= a_sorted[i][0]
	if x >= 0:
		count += 1
	i += 1
if x - a_sorted[i][0] == 0:
	count += 1
print(count)
