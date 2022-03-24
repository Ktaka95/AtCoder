N, M = map(int, input().split())
es = list()

for _ in range(M):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	es.append((a, b))

parent = None
def root(a):
	if parent[a] == a:
		return a
	else:
		parent[a] = root(parent[a])
		return parent[a]

def is_same(a, b):
	return root(a) == root(b)

def unite(a, b):
	ra = root(a)
	rb = root(b)
	if ra == rb: return
	parent[ra] = rb;

ans = 0
for i in range(M):
	parent = [k for k in range(N)]
	for j, e in enumerate(es):
		if j == i: continue
		a, b = e
		unite(a, b)
	a, b = es[i]
	if not is_same(a, b):
		ans += 1
print(ans)
