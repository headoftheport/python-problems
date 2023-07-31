from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        topological sort solution
        tc: numCourses + numPrerequisites
        sc: numCourses
        """
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
                
        ans = []
        
        while queue:
            
            node = queue.popleft()
            ans.append(node)
            
            for nex in adj[node]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    queue.append(nex)
                    
        if len(ans) != numCourses:
            return []
        
        return ans


    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        """
        dfs solution
        tc: numCourses + numPrerequisites
        sc: numCourses
        """
         
        adj = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        
        ans = []
        for i in range(numCourses):
            if not self.dfs(i, adj, visited, ans):
                return []
        return ans
    
    def dfs(self, node, adj, visited, ans):
        
        if visited[node] == -1:
            return False
        
        if visited[node] == 1:
            return True
        
        visited[node] = -1
        for nex in adj[node]:
            if not self.dfs(nex, adj, visited, ans):
                return False
            
        ans.append(node)
        visited[node] = 1
        return True