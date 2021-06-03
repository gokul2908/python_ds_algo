from collections import deque


class stack:
    def __init__(self) -> None:
        self.__arr = deque([])

    def put(self, element):
        self.__arr.appendleft(element)
        return

    def get(self):
        return self.__arr.pop()


cls = stack()
cls.put(5)
cls.put(54)
cls.put(52)
cls.put(56)
cls.put(58)
cls.put(59)

print(cls.get())
print(cls.get())
print(cls.get())
print(cls.get())
print(cls.get())
print(cls.get())
