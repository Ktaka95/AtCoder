N, A, B = map(int, input().split())

Ncpy = N
div = 0
for _ in range(4):
	Ncpy = Ncpy / 10
	if Ncpy >= 1:
		div += 1
factor = 0
sum = 0
for i in range(1, N + 1):
	for j in range(div, -1, -1):
		factor += i // (10 ** div)
		i %= (10 ** div)
	if A <= factor <= B:
		sum += factor
print(sum)
