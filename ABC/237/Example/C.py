S = input()

a_cnt = 0
for c in S:
	if c == 'a':
		a_cnt += 1
if a_cnt == len(S):
	print("Yes")
	exit()

lefta = 0
righta = 0

while S[lefta] == 'a':
	lefta += 1
while S[-(righta+1)] == 'a':
	righta += 1

middle = S[lefta:len(S)-righta]
print(lefta, righta, middle)
if middle == middle[::-1] and lefta <= righta:
	print("Yes")
else:
	print("No")
