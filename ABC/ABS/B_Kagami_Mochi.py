N = int(input())
d = [0] * N
for i in range(N):
	d[i] = int(input())
d_set = set(d)
print(len(d_set))
