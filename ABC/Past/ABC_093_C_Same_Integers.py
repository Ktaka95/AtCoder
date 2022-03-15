A, B, C = map(int, input().split())

min = min(A, B, C)
max = max(A, B, C)
middle = A + B + C - min - max

if min % 2 == middle % 2 == max % 2:
	count = (max - min) // 2 + (max - middle) // 2
elif min % 2 == middle % 2:
	count = (middle - min) // 2 + max - middle
elif min % 2 == max % 2:
	count = (max - min) // 2 + (max - middle) // 2 + 2
else:
	count = (max - min) // 2 + 1 + (max - middle) // 2 + 1
print(count)
