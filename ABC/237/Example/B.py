H, W = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]

for row in zip(*mat):
	print(*row)
