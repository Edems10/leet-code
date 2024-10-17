import random

class RandomizedSet:
    def __init__(self):
        self.my_set = set()
        self.my_list = []

    def insert(self, val):
        if val not in self.my_set:
            self.my_set.add(val)
            self.my_list.append(val)
            return True
        return False

    def remove(self, val):
        if val in self.my_set:
            self.my_set.remove(val)
            self.my_list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
