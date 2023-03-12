class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root_node = self.buildTrie(words)
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, ans, root_node)
                
        return ans
    
    def dfs(self, board, row, col , ans, root):
        
        char = board[row][col]
        if char == '#' or root.next[ord(char)- ord('a')] == None:
            return
        
        root = root.next[ord(char)-ord('a')]
        
        if root.word != None:
            ans.append(root.word)
            root.word = None
            
        board[row][col] = '#'
            
        if row > 0:
            self.dfs(board, row - 1, col, ans, root)
            
        if row < len(board)-1:
            self.dfs(board, row + 1, col, ans, root)
            
        if col > 0:
            self.dfs(board, row, col - 1, ans, root)
            
        if col < len(board[0])-1:
            self.dfs(board, row, col + 1, ans, root)
            
        board[row][col] = char
        
        
    def buildTrie(self, words):
        root = Solution.TrieNode()
        for word in words:
            curr = root
            for char in word:
                index = ord(char) - ord('a')
                if curr.next[index] == None:
                    curr.next[index] = Solution.TrieNode()
                curr = curr.next[index]
            curr.word = word
            
        return root
        
        
        
    class TrieNode:
        
        def __init__(self):
            self.next = [None for i in range(26)]
            self.word = None
        