S1, S2, S3 = map(str, input().split())
T1, T2, T3 = map(str, input().split())

if S1 == T1 and S2 == T2:
	flag = True
elif S1 == T1 and S2 == T3:
	flag = False
elif S1 == T2 and S2 == T3:
	flag = True
elif S1 == T3 and S2 == T2:
	flag = False
elif S1 == T2 and S2 == T1:
	flag = False
elif S1 == T3 and S2 == T1:
	flag = True
print("Yes" if flag else "No")
