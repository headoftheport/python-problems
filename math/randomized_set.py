import random
class RandomizedSet:

    def __init__(self):
        self.values = list()
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values.append(val)
        self.index_map[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
            
        index, last = self.index_map[val], len(self.values) - 1
        self.values[index], self.values[last] = self.values[last], self.values[index]
        self.index_map[self.values[index]] = index
        self.values.pop()
        del self.index_map[val]
        return True
        

    def getRandom(self) -> int:
        rand = random.randrange(len(self.values))
        return self.values[rand]
                          
                          
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()