"""keys and rooms"""
class Solution:
    """solution"""
    def can_visit_all_rooms(self, rooms) -> bool:
        """using dfs traversal"""
        #time complexity of o(n + e)
        #space complexity of o(n)
        visited = [False for i in range(len(rooms))]
        
        self.dfs(rooms, 0, visited)
        
        for i in visited:
            if i is False:
                return False
            
        return True
        
        
    def dfs(self, rooms, source, visited):
        """dfs"""
        if visited[source]:
            return
        
        visited[source] = True
        for key in rooms[source]:
            self.dfs(rooms, key, visited)
            
        return
    