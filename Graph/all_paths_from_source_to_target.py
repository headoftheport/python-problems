"""all paths from source to target"""
class Solution:
    """solution"""
    def all_paths_source_to_target(self, graph):
        """DFS using stack """
        if not graph:
            return []

        d = {}
        for item, value in enumerate(graph):
            d[item] = value
        stack = [[0,[0]]]
        n = len(graph)
        res = []
        while stack:
            node, path = stack.pop()
            if node == n-1:
                res.append(path)
            
            for nei in d[node]:
                stack.append([nei, path.append(nei)])

        return res