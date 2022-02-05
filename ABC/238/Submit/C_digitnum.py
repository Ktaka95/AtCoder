N = int(input())

N_str = str(N)
digit = len(N_str)
total = 0

for i in range(digit - 1):
	total += 45 * (10 ** i)
tmp = N - 10 ** (digit - 1) + 1
mod = tmp + total
print(mod % 998244353)
