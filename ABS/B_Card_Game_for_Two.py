N = int(input())
a = list(map(int,input().split()))
if N % 2 == 1:
	a.append(0)
	N += 1
a_sort = sorted(a, reverse=True)
alice = 0
bob = 0

for i in range(0, N - 1, 2):
	alice += a_sort[i]
	bob += a_sort[i + 1]
print(alice - bob)
