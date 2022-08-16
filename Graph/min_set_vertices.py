"""solved using topological sorting"""

from collections import defaultdict

class Solution:
    """solution"""
    def find_smallest_set_of_vertices(self, n: int, edges):
        """ answer """
        #time complexity O(E+V)
        #space complexity O(n) + O(n) + O(n^2)
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        
        stack = list()
        visited = [False for i in range(n)]
        
        for i in range(n):
            self.top_sort(graph, i, visited, stack)
        
        visited = [False for i in range(n)]
        store = list()
        while stack:
            node = stack.pop()
            if not visited[node]:
                self.dfs(graph, node, visited)
                store.append(node)
                
        return store
                
           
    def top_sort(self, graph, node, visited, stack):
        """topological sorting"""
        if visited[node]:
            return
        
        visited[node] = True
        
        for item in graph[node]:
            self.top_sort(graph, item, visited, stack)
            
        stack.append(node)
        
        
    def dfs(self, graph, node, visited):
        """dfs"""
        if visited[node]:
            return
        
        visited[node] = True
        
        for item in graph[node]:
            self.dfs(graph, item, visited)
        
        
        
        