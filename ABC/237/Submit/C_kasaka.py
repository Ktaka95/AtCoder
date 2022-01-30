S_reverse = input()
S = S_reverse[::-1]
i = 0
a_cnt = 0

if S == S_reverse:
	print("Yes")
elif S_reverse.startswith("a"):
	while True:
		a = "a"
		a_cnt = 0
		S_reverse.startswith(a_cnt)
		a += "a"
		a_cnt += 1
		print(a_cnt)
else:
	print("No")

# cnt = len(S)
# S_reverse = [0] * cnt
# i = 0
# a_cnt = 0


# if S == S_reverse:
# 	print("Yes")
