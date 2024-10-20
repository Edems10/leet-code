class AllOne:

    def __init__(self):
        self.all = {}
        self.max = float("-inf")
        self.max_name = ""
        self.min = float("inf")
        self.min_name = ""

    def inc(self, key: str) -> None:
        key = str(key[0])
        found = self.all.get(key)
        if found:
            self.all[key] = found + 1
        else:
            self.all[key] = 1
        count = self.all.get(key)
        self.recalculate_min_max(count, key)
        return

    def recalculate_min_max(self, count, key) -> None:
        if self.max < count:
            self.max = count
            self.max_name = key
        if self.min > count:
            self.min = count
            self.min_name = key

    def dec(self, key: str) -> None:
        key = str(key[0])
        found = self.all.get(key)
        if found != 1:
            self.all[key] = found - 1
        else:
            self.all.pop(key)
        count = self.all.get(key)
        self.recalculate_min_max(count, key)
        return

    def getMaxKey(self) -> str:
        return self.max_name

    def getMinKey(self) -> str:
        return self.min_name


if __name__ == "__main__":
    a1 = [
        "AllOne",
        "inc",
        "inc",
        "getMaxKey",
        "getMinKey",
        "inc",
        "getMaxKey",
        "getMinKey",
    ]
    a2 = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]

    for arg1, arg2 in zip(a1, a2):
        if arg1 == "AllOne":
            obj = AllOne()
        elif arg1 == "inc":
            print(obj.inc(arg2))
        elif arg1 == "getMaxKey":
            print(obj.getMaxKey())
        elif arg1 == "getMinKey":
            print(obj.getMinKey())
