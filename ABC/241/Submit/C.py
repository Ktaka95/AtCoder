N = int(input())

dp = list()
flag = False
for i in range(N):
	S = list(input())
	dp.append(S)
	for i in range(N - 5):
		w_count = 0
		for k in range(6):
			if S[i + k] == '#':
				w_count += 1
			if w_count >= 4:
				flag = True
if flag:
	print("Yes")
else:
	for i in range(N - 5):
		for j in range(N - 5):
			h_count = 0
			c_count = 0
			for k in range(6):
				if dp[i + k][j] == '#':
					h_count += 1
				if dp[i + k][j + k] == '#':
					c_count += 1
			if h_count >= 4 or c_count >= 4:
				flag = True
	if flag:
		print("Yes")
	else:
		print("No")
