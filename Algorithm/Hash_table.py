class hash:
    def __init__(self) -> None:
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def hash_function(self, key):
        max = 10
        x = 0
        for character in key:
            x += ord(character)
        return x % max

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        if len(self.arr[index]) > 0:
            for index_1, element in enumerate(self.arr[index]):
                if element[0] == key:
                    self.arr[index][index_1] = (key, value)
                    return
            self.arr[index].append((key, value))
            return
        self.arr[index].append((key, value))

    def __getitem__(self, key):
        index = self.hash_function(key)
        for element in self.arr[index]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key: str) -> None:
        index = self.hash_function(key)
        del self.arr[index]


# home = hash()
# home["march 17"] = "Rs.200"
# print(home.arr)
# home["march 6"] = "Rs. 99"
# print(home.arr)
# # del home["march 17"]
# print(home["march 6"])
