class MyHashSet:

    def __init__(self):
        self.hashset = []
        

    def add(self, key: int) -> None:
        for element in self.hashset:
            if element == key:
                return

        self.hashset.append(key)

    def remove(self, key: int) -> None:
        for element in self.hashset:
            if element == key:
                self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        for element in self.hashset:
            if element == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)