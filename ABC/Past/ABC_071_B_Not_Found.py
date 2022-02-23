S = set(input())
alphabet_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

alphabet_not_in_S = set()
for alphabet in alphabet_set:
	if alphabet not in S:
		alphabet_not_in_S.add(alphabet)
if len(alphabet_not_in_S) != 0:
	print(min(alphabet_not_in_S))
else:
	print("None")
