class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        graph = defaultdict(dict)
        
        for equation,value in zip(equations, values):
            v = equation[0]
            u = equation[1]
            graph[v][v] = 1.0
            graph[u][u] = 1.0
            graph[v][u] = value
            graph[u][v] = 1/value
            
        for k, i, j in itertools.permutations(graph,3):
            if k in graph[i] and j in graph[k]:
                graph[i][j] = graph[i][k] * graph[k][j]
                
        return [graph[source].get(dest, -1.0) for (source, dest) in queries]
        