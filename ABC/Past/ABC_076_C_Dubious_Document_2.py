import re

S = input()
T = input()

len_s = len(S)
len_t = len(T)

if len_s < len_t:
	print("UNRESTORABLE")
	exit()
S = S.replace('?', '.')
ans = []
for i in range(len_s - len_t + 1):
	m = re.match(S[i:i + len_t], T)
	if m is None:
		continue
	ans.append((S[:i] + T + S[i + len_t:]).replace('.', 'a'))
if not ans:
	print("UNRESTORABLE")
	exit()
print(min(ans))

