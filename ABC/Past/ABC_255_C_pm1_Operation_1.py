X, A, D, N = map(int, input().split())

diff = abs(A - X)
for i in range (N):
    s = A + D * i
    tmp_diff = abs(X - s)
    if tmp_diff < diff:
        diff = tmp_diff
print(diff)
