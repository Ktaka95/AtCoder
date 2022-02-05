MOD = 998244353
N = int(input())

def nC2(n):
	return n * (n - 1) // 2

ans = N
for k in range(1, 20):
	bottom = 10 ** (k - 1)
	top = 10 ** k

	if N < bottom:
		break
	elif top <= N:
		ans += top - bottom
	else:
		ans += N + 1 - top

print(ans % MOD)
