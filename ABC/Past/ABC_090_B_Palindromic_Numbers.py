A, B = map(int, input().split())
count = 0

for i in range(A, B + 1):
	itoa = str(i)
	if itoa == itoa[::-1]:
		count += 1
print(count)
