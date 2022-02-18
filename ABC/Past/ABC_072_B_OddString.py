s = input()

new_s_len = len(s) // 2 + len(s) % 2
new_s = [0] * new_s_len
j = 0

for i in range(len(s)):
	if i % 2 == 0:
		new_s[j] = s[i]
		j += 1
print(*new_s, sep='')
