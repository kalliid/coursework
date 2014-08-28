def BFS(s, Adj):
    level = {S : 0}
    parent = {S : None}
    i = 1
    frontier = [S]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

parent = {s : None}
def DFS_visit(V, adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_visit(V, Adj, s)

def DFS(V, adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(V, adj, s)

