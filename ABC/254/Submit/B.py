N = int(input())

a = [[1] * (i + 1) for i in range (N)]
for i in range(0, N):
    for j in range (0, i+1):
        if j == 0 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j - 1] + a[i-1][j]
    print(*a[i])
