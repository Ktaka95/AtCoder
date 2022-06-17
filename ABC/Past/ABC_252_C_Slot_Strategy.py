N = int(input())

S = list()
for i in range(N):
    S.append(input())

sec = [0] * 10
for s in S:
    for i in range(10):
        sec[i] = max(sec[i], s.index(str(i)))
print(sec)
