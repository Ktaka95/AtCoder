N = int(input())
A = list(map(int, input().split()))


if A[0] >= 180:
	max_pizza = A[0]
else:
	max_pizza = 360 - A[0]
limit = 360 - A[0]
turn_total = A[0]
i = 1
for i in range(N):
	limit -= A[i]
	turn_total += A[i]
	if turn_total > limit:
		max_pizza -= A[i]

print(max_pizza)

