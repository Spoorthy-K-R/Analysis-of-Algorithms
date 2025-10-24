def make_set(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def find(parent, x):
    # path compression
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False  # already connected
    # union by rank
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
    return True

def contains_cycle(V, edges):
    parent, rank = make_set(V)
    seen = 0
    for u, v in edges:
        if u == v:
            return True
        if find(parent, u) == find(parent, v):
            return True
        union(parent, rank, u, v)
        seen += 1
        if seen == V:
            return True
    return False


# ---- Test cases ----
tests = [
    # 1) Acyclic tree on 5 vertices (a line)
    dict(V=5, E=[(0,1),(1,2),(2,3),(3,4)], expect=False, name="Tree (acyclic)"),

    # 2) Single 3-cycle (triangle)
    dict(V=4, E=[(0,1),(1,2),(2,0)], expect=True, name="Triangle cycle"),

]

ok = True
for i, t in enumerate(tests, 1):
    has = contains_cycle(t["V"], t["E"])
    print(f"[{i}] {t['name']:<28}  V={t['V']}, E={t['E']}\n    -> contains_cycle = {has}  (expected {t['expect']})\n")
    ok &= (has == t["expect"])

print("All tests passed!" if ok else "Some tests failed.")