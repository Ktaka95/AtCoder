A, B, C, D = map(int, input().split())

takahashi = list()
aoki = list()

for i in range(A, B + 1):
	takahashi.append(i)
for i in range(C, D + 1):
	aoki.append(i)

prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199}

check = list()
for i in range(len(takahashi)):
	for j in range(len(aoki)):
		if (takahashi[i] + aoki[j]) in prime:
			check.append(0)
			break

if len(check) == len(takahashi):
	print("Aoki")
else:
	print("Takahashi")
