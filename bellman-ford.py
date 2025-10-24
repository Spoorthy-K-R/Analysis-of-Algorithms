from math import inf

def bellman_ford_early_stop(V, edges, s):
    dist = [inf]*V
    dist[s] = 0.0
    passes = 0

    while True:
        changed = False
        passes += 1
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:          # nothing improved -> stop (this is the early-stop)
            return dist, passes, False
        if passes >= V:          # did V passes -> if problem’s precondition holds, we should have halted earlier
            return dist, passes, True

def bellman_ford_full(V, edges, s):
    dist = [inf]*V
    dist[s] = 0.0
    for _ in range(V-1):
        improved = False
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                improved = True
        if not improved:
            break
    # detect negative cycle reachable from s
    has_neg = False
    for (u, v, w) in edges:
        if dist[u] + w < dist[v]:
            has_neg = True
            break
    return dist, has_neg

