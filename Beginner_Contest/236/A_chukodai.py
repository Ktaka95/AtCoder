str = input()
a, b = map(int, input().split())

for i in range(a - 1):
	print(str[i], end='')
print(str[b - 1], end='')
for i in range(a, b - 1):
	print(str[i], end='')
print(str[a - 1], end='')
for i in range(b, len(str)):
	print(str[i], end='')
