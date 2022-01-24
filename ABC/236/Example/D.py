from msilib.schema import tables
import pickletools
from tkinter.messagebox import YESNOCANCEL


N = int(input())
A = [0] * (2*N)
for i in range(2*N-1):
	A[i] = list(map(int, input().split()))

ans = 0

def calc(dancer, score):
	if len(dancer) == 0:
		global ans
		ans = max(ans)
		return score
	for i in range(len(dancer) - 1):
		for i
