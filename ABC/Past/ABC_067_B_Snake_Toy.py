N, K = map(int, input().split())
l = list(map(int, input().split()))

sorted_l = sorted(l, reverse=True)
max_l = sorted_l[:K]
print(sum(max_l))
