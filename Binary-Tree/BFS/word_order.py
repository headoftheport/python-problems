from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        """
        space complexity: O( m^2 * n)
        time complexity: O(m^2 * n ) 
        """
        word_length = len(beginWord)
        store = {}

        for word in wordList:
            for i in range(word_length):
                string = word[:i] + '*' + word[i+1:]
                if string not in store:
                    store[string] = []
                store[string].append(word)

        queue = deque()
        queue.append(beginWord)
        step = 1
        visited = {beginWord: True}
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                for i in range(word_length):
                    string = word[:i] + '*' + word[i+1:]
                    if string not in store:
                        continue

                    for temp in store[string]:
                        if temp == endWord:
                            return step + 1

                        if temp not in visited:
                            visited[temp] = True
                            queue.append(temp)
            step = step + 1

        return 0


    def ladderLength2(self, beginWord: str, endWord: str, wordList): 

        words = set(wordList)
        queue = deque()
        queue.append(beginWord)
        step = 1
        while queue:
            length = len(queue)
            for i in range(length):
                curr_word = queue.popleft()
                array = list(curr_word)
                for i in range(len(array)):
                    char = array[i]
                    start = ord('a')
                    for j in range(26):
                        curr = chr(start + j)
                        array[i] = curr
                        string = ""
                        string = string.join(array)
                        if string in words and string == endWord:
                            return step + 1
                        
                        if string in words:
                            queue.append(string)
                            words.remove(string)
                            
                    array[i] = char
                            
            step += 1
            
        return 0



         
        