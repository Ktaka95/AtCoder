from collections import defaultdict

import heapq

Q = int(input())

Count = defaultdict(int)

MaxQue = []
MinQue = []

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        Count[x] += 1
        heapq.heappush(MinQue, x)
        heapq.heappush(MaxQue, -x)
    elif query[0] == 2:
        x = query[1]
        c = query[2]
        Count[x] -= min(c, Count[x])
    else:
        SMin = heapq.heappop(MinQue)
        while Count[SMin] == 0:
            SMin = heapq.heappop(MinQue)
        SMax = heapq.heappop(MaxQue)
        SMax *= -1
        while Count[SMax] == 0:
            SMax = heapq.heappop(MaxQue)
            SMax *= -1
        print(SMax - SMin)
        
        heapq.heappush(MinQue, SMin)
        heapq.heappush(MaxQue, -SMax)

# my_solve
# Q = int(input())

# S = list()

# for i in range(Q):
#     q = list(map(int, input().split()))
#     if q[0] == 1:
#         S.append(q[1])

#     elif q[0] == 2:
#         del_itr = min(q[2], S.count(q[1]))
#         for i in range (del_itr):
#             S.remove(q[1])
#     else:
#         print(max(S) - min(S))
