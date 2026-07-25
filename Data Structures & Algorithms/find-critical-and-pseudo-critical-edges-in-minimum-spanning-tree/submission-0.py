class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # CHANGED: store original index before sorting
        edges = [edge + [i] for i, edge in enumerate(edges)]

        # Kruskal requires sorted edges
        edges.sort(key=lambda x: x[2])

        def Kruskals(edge, skip, force):

            # CHANGED: Fresh Union Find for EVERY run
            parents = list(range(n))
            rank = [0] * n

            def find(x):
                if x != parents[x]:
                    parents[x] = find(parents[x])
                return parents[x]

            def union(n1, n2):
                p1, p2 = find(n1), find(n2)
                if p1 == p2:
                    return False

                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                elif rank[p2] > rank[p1]:
                    parents[p1] = p2
                else:
                    parents[p1] = p2
                    rank[p2] += 1
                return True

            nodes = 0
            weight = 0

            # CHANGED: Force edge FIRST
            if force:
                a, b, w, idx = edge
                union(a, b)
                weight += w
                nodes += 1

            # CHANGED: Single Kruskal loop for all 3 modes
            for a, b, w, idx in edges:

                # CHANGED: skip the forbidden edge
                if skip and idx == edge[3]:
                    continue

                # CHANGED: don't process forced edge twice
                if force and idx == edge[3]:
                    continue

                if union(a, b):
                    weight += w
                    nodes += 1

            # CHANGED: Graph disconnected
            if nodes != n - 1:
                return float("inf")

            return weight

        # CHANGED: Compute original MST using helper itself
        minWeight = Kruskals(None, False, False)

        critical = []
        pseudoCritical = []

        for edge in edges:

            idx = edge[3]

            # Critical test
            if Kruskals(edge, True, False) > minWeight:
                critical.append(idx)

            # CHANGED: Actually compare the forced MST weight
            elif Kruskals(edge, False, True) == minWeight:
                pseudoCritical.append(idx)

        return [critical, pseudoCritical]