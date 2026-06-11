class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        V = 0
        for u, v in edges:
            V = max(V, u, v)

        adj = [[] for _ in range(V + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0

        def dfs(st, vis, c):
            nonlocal count
            count = max(c, count)

            for val in adj[st]:
                if val not in vis:
                    vis.add(val)
                    dfs(val, vis, c + 1)

        vis = set()
        vis.add(1)
        dfs(1, vis, 0)

        return pow(2, count - 1, MOD) if count > 0 else 1