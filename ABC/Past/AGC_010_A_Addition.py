N = int(input())
A = list(map(int, input().split()))

odd_count = 0
for a in A:
	if a % 2 == 1:
		odd_count += 1
if odd_count % 2 == 1:
	print("NO")
else:
	print("YES")
