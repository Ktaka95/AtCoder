# N = int(input())
# T, A = map(int, input().split())
# H = list(map(int, input().split()))
# old_diff = A - (T - H[0] * 0.006)
# ret = 1

# for i in range(1, N):
# 	H_temp = T - H[i] * 0.006
# 	diff = abs(A - H_temp)
# 	if diff < old_diff:
# 		ret = i + 1
# 		old_diff = diff
# print(ret)

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff = set()

for i in range(N):
	diff_H = abs(A - (T - H[i] * 0.006))
	diff.add(diff_H)
	if min(diff) == diff_H:
		ret = i + 1
print(ret)
