N, A, B = map(int, input().split())

Ncpy = N
div = 0
for _ in range(4):
	Ncpy = Ncpy / 10
	if Ncpy >= 1:
		div += 1
sum = 0
for i in range(1, N + 1):
	factor = 0
	icpy = i
	for j in range(div, -1, -1):
		factor += icpy // (10 ** j)
		icpy %= (10 ** j)
	if A <= factor <= B:
		sum += i
print(sum)
