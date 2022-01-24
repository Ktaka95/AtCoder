N = int(input())
hold_card = list(map(int, input().split()))
i = 1
all_card = 0
for i in range(1, N + 1):
	for _ in range(4):
		all_card += i
hold_card_sum = 0
for _ in range(4*N - 1):
	hold_card_sum += hold_card[_]
result = all_card - hold_card_sum
print(result)
