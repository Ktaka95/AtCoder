N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
min_a = min(A)

print(max(A) - min(A))
