s = input()

for i in range(len(s)):
	if s[i] == 'A':
		start = i
		break
for j in range(1, len(s)):
	if s[-j] == 'Z':
		end = len(s) - j
		break
print(end - start + 1)
