# for graphs

def bfs(s, adj):
    level = {'s':0}
    parent = {'s': None}
    i = 1
    frontier = [s]

    while frontier:
        next = []
        for u in frontier:
            for v in adj:
                if v not in level:
                    level[v] = 1
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1