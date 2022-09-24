"""course schedule"""
from collections import deque


class Solution:
    """solution"""
    def can_finish(self, numCourses, prerequisites):
        """
        topological sorting to find cycle
        time: O(E + V)
        sapce: O(E + V)
        """
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            adj[req].append(course)
            indegree[course] += 1

        queue = deque()
        for index, count in enumerate(indegree):
            if count == 0:
                queue.append(index)
        
        edge_count = len(prerequisites)
        while queue:
            curr = queue.popleft()
            for nex in adj[curr]:
                edge_count -= 1
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    queue.append(nex)

        return edge_count == 0
        

    def can_finish2(self, numCourses, prerequisites):
        """
        dfs to find the cycle in directted graph
        time: O(E+V)
        space: O(E+V)
        """
        adj = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            adj[req].append(course)


        def dfs(adj, visited, curr):
            if visited[curr] == -1:
                return False

            if visited[curr] == 1:
                return True

            visited[curr] = -1 
            for nex in adj[curr]:
                if not dfs(adj, visited, nex):
                    return False

            visited[curr] = 1
            return True

        for item in range(numCourses):
            if visited[item] == 0 and (not dfs(adj, visited, item)):
                return False
        return True

        


