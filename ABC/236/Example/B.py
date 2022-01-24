N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N+1)	# カウント用の配列を用意、0は今回使わない

for a in A:	# 配列Aを一つずつ取り出す
	cnt[a] += 1	# 該当する数のカウントを1つ増やす

for i in range(1, N+1):
	if cnt[i] == 3: # 1~Nまでの数のカウントを確認
		print(i)
