class LRUCache:
    
    class Node:
        
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            
            
    class DoubleLinkedList:
        
        def __init__(self):
            self.head = LRUCache.Node(0,0)
            self.tail = LRUCache.Node(0,0)
            
            self.head.next = self.tail
            self.tail.prev = self.head
            
        
        def addNode(self, node):
            
            node.prev = self.head
            node.next = self.head.next
            
            self.head.next.prev = node
            self.head.next = node
            
        def removeNode(self, node):
            
            pre = node.prev
            nex = node.next
            
            pre.next = nex
            nex.prev = pre
            
        def movetoHead(self, node):
            
            self.removeNode(node)
            self.addNode(node)
            
        def popTail(self):
            
            node = self.tail.prev
            self.removeNode(node)
            return node
            

    def __init__(self, capacity: int):
        
        self.size = 0
        self.capacity = capacity
        self.list = LRUCache.DoubleLinkedList()
        self.store = {}

    def get(self, key: int) -> int:
        
        if key not in self.store:
            return -1
        
        node = self.store.get(key)
        self.list.movetoHead(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.store:
            
            node = self.store.get(key)
            node.value = value
            self.list.movetoHead(node)
            
        else:
            
            node = LRUCache.Node(key, value)
            self.list.addNode(node)
            self.size = self.size + 1
            self.store[key] = node
            if self.size > self.capacity:
                node = self.list.popTail()
                del self.store[node.key]
                self.size -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)