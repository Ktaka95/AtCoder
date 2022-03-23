def inversion_parity(s):
	ans = 0
	for i in range(3):
		for j in range(i + 1, 3):
			if s[i] > s[j]:
				ans += 1
	return ans % 2

S = input().split()
T = input().split()

if inversion_parity(S) == inversion_parity(T):
	print("Yes")
else:
	print("No")
