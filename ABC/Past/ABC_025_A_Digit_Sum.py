N = int(input())
pow_10 = set()

for i in range(1, 6):
	pow_10.add(pow(10, i))
if N in pow_10:
	print(10)
else:
	itoa_n = list(str(N))
	digit_list = list(map(int, itoa_n))
	print(sum(digit_list))
