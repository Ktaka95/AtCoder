A, B, C, X, Y = map(int, input().split())

standard = A * X + B * Y
if X == Y:
	tmp = C * 2 * X
elif X > Y:
	tmp_1 = C * 2 * Y + A * (X - Y)
	tmp_2 = C * 2 * X
	tmp = min(tmp_1, tmp_2)
else:
	tmp_1 = C * 2 * X + B * (Y - X)
	tmp_2 = C * 2 * Y
	tmp = min(tmp_1, tmp_2)
print(min(standard, tmp))
