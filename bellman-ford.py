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

def pretty(dist):
    return ["inf" if d == inf else f"{d:g}" for d in dist]

# ---------------------- Test graphs ----------------------

tests = []

# 1) Non-negative weights, simple
tests.append(dict(
    name="Simple non-negative",
    V=5,
    E=[(0,1,3),(0,2,1),(2,1,1),(1,3,2),(2,3,4),(3,4,1)],
    s=0
))

# 2) Negative edges but no negative cycle
tests.append(dict(
    name="Negative edges, no cycle",
    V=5,
    E=[(0,1,6),(0,2,7),(1,2,8),(1,3,5),(1,4,-4),(2,3,-3),(2,4,9),(3,1,-2),(4,3,7),(4,0,2)],
    s=0
))

# 3) Unreachable nodes
tests.append(dict(
    name="Unreachable vertices",
    V=6,
    E=[(0,1,2),(1,2,2),(2,3,2)],
    s=0
))

# ---------------------- Run tests ----------------------

for i, t in enumerate(tests, 1):
    V, E, s = t["V"], t["E"], t["s"]
    dist_ref, neg = bellman_ford_full(V, E, s)
    dist_es, passes, flag = bellman_ford_early_stop(V, E, s)

    print(f"[{i}] {t['name']}")
    if neg:
        print("(Reference BF reports a negative cycle reachable from source — test violates precondition.)")
    print(f"source = {s}, passes (early-stop) = {passes}")
    print(f"ref distances : {pretty(dist_ref)}")
    print(f"es  distances : {pretty(dist_es)}")
    if not neg:
        ok = all((a == b) or (a != a and b != b) for a,b in zip(dist_ref, dist_es)) \
             or all((a == inf and b == inf) for a,b in zip(dist_ref, dist_es))
        ok = all((dr == inf and de == inf) or abs((dr or 0) - (de or 0)) < 1e-9 for dr,de in zip(dist_ref, dist_es))
        print(f"match with reference? {'YES' if ok else 'NO'}")
    print()