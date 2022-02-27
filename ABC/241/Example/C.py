N = int(input())

S = [input() for _ in range(N)]

dxs = [0, 1, 1, 1]
dys = [1, 1, 0, -1]

for i in range(N):
	for j in range(N):
		for d in range(4):
			dx = dxs[d]
			dy = dys[d]
			white_cnt = 0
			for k in range(6):
				nx = i + dx * k
				ny = i + dy * k
				if not (0 <= nx < N and 0 <= ny < N):
					white_cnt = 100
					break
				if S[nx][ny] == '.':
					white_cnt += 1
			if white_cnt <= 2:
				print("Yes")
				exit()
print("No")
