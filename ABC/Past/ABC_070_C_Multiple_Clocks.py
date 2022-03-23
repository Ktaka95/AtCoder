import math
from functools import reduce

N = int(input())
T = set()
for i in range(N):
	T.add(int(input()))

def lcm_base(x, y):
	return (x * y) // math.gcd(x, y)

def lcm_recursive(*numbers):
	return reduce(lcm_base, numbers)

print(lcm_recursive(*T))
