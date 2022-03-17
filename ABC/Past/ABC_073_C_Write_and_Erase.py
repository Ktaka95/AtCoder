N = int(input())

card = set()
for i in range(N):
	a = int(input())
	if a in card:
		card.remove(a)
	else:
		card.add(a)
print(len(card))
