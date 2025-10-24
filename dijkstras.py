import heapq
from collections import defaultdict

# --------complete the edge list from the map --------
EDGES = [
    (1,2,1), (1,11,1), 
    (2,3,1), (3,4,1), (21, 22, 2), (2, 21, 1),
    (3,4,1), (3,8,2),
    (4,5,1), (5,7,1), (5,6,2), (5,22,1),
    (6,7,2),
    (7,8,1),
    (8,9,1),
    (9,10,1), (9,19,1), (16, 17, 2), (17, 18,2),
    (10, 11,1), (10, 18,2),
    (11, 12, 2), (11, 17, 1),
    (12, 13, 2),
    (13, 14, 2),
    (13, 21, 1),
    (14, 15, 1), (14, 16, 1), (14, 20, 1),
    (20, 22, 1), (21, 20, 2)
]

DESTS = [6,8,9,15,16,22]
N = 22 

adj = defaultdict(list)
for u,v,w in EDGES:
    adj[u].append((v,w))
    adj[v].append((u,w))

def dijkstra(src: int):
    INF = 10**9
    d = [INF]*(N+1)
    d[src] = 0
    pq = [(0, src)]
    visited = [False]*(N+1)
    while pq:
        du,u = heapq.heappop(pq)
        if visited[u]: 
            continue
        visited[u] = True
        for v,w in adj[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                heapq.heappush(pq, (d[v], v))
    return d

d = dijkstra(1)
for t in DESTS:
    val = d[t] if d[t] < 10**9 else None
    print("Distance from 1 to", t, "is", val)
    print(f"d(1→{t}) = {val}")