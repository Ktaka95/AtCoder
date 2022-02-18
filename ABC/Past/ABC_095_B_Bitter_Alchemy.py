N, X = map(int, input().split())
m_list = list()
for i in range(N):
	m = int(input())
	X -= m
	m_list.append(m)
extra = X // min(m_list)
print(N + extra)
