import math

N = int(input())

min_b_digit = len(str(N))
for i in range(1, math.floor(math.sqrt(N)) + 1):
	if N % i == 0:
		new_b = N // i
		if len(str(new_b)) < min_b_digit:
			min_b_digit = len(str(new_b))
print(min_b_digit)
