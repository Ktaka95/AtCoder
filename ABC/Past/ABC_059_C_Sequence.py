n = int(input())
a = list(map(int, input().split()))

even_plus_count = 0
new_sum = 0
for i in range (n):
	new_sum += a[i]
	if i % 2 == 0:
		if new_sum <= 0:
			even_plus_count += abs(new_sum) + 1
			new_sum = 1
	else:
		if new_sum >= 0:
			even_plus_count += new_sum + 1
			new_sum = -1
odd_plus_count = 0
new_sum = 0
for j in range (n):
	new_sum += a[j]
	if j % 2 != 0:
		if new_sum <= 0:
			odd_plus_count += abs(new_sum) + 1
			new_sum = 1
	else:
		if new_sum >= 0:
			odd_plus_count += new_sum + 1
			new_sum = -1
print(min(even_plus_count, odd_plus_count))
