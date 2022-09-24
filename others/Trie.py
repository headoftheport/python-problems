"""creation of trie data structure"""
class TrieNode:
    """node"""
    def __init__(self) -> None:
        """init method"""
        self.values = [None for _ in range(26)]
        self.end = False


    def contains_key(self,val):
        """ to check if the val in current node"""
        return self.values[ord(val) - 97] is not None

    def set_key(self, val):
        """set the trie key"""
        if self.values[ord(val)-97] is None:
            self.values[ord(val)-97] = TrieNode()

        return self.values[ord(val)]

    def get_key(self, val):
        """get a next node"""
        return self.values[ord(val)-97]

    def set_end(self):
        """set the node as end"""
        self.end = True

    def is_end(self):
        """is the node end"""
        return self.end


class Trie:
    """trie class"""
    def __init__(self) -> None:
        self.root = TrieNode()


    def insert(self, word):
        """insert"""
        node = self.root
        for index, val in enumerate(word):
            node = node.set_key(val)
        node.set_end()

    def starts_with_word(self, word):
        """starts with"""
        node = self.root
        for index, val in enumerate(word):
            if not node.contains_key(val):
                return None
            node = node.get_key(val)
        return node

    def starts_with(self, word):
        """starts with"""
        node = self.starts_with_word(word)
        return node is not None

    def search(self, word):
        """search"""
        node = self.starts_with(word)
        return node is not None and node.is_end()
        


