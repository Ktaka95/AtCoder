import sys

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = map(int, input().split())

eat_list = set()
eat = max(A)
for i in range(N):
    if A[i] == eat:
        eat_list.add(i + 1)

for b in B:
    if b in eat_list:
        print("Yes")
        sys.exit()
print("No")
