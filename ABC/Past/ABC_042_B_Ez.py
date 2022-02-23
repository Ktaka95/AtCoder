N, L = map(int, input().split())

s_list = list()
for _ in range(N):
	s_list.append(input())
print(*sorted(s_list), sep='')
