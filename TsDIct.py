import math
import threading


class TsDict:
    lock = threading.Lock()

    def __init__(self):
        self.size = 10
        self.occupied = 0
        self.list = [list() for _ in range(10)]

    def __find_index__(self, key):
        return abs(hash(key) % len(self.list))

    def __rehash__(self):
        if 0.75 * len(self.list) <= self.occupied:
            self.list.extend([list() for _ in range(len(self.list) * 2)])
            for element in self.list:
                if len(element) != 0:
                    self.put(element[0], element[1])

    def put(self, key, value):
        index = self.__find_index__(key)
        if len(self.list[index]) != 0:
            for i in range(0, len(self.list[index])):
                if self.list[index][i][0] == key:
                    self.list[index][i] = tuple([self.list[index][i][0], value])
                    return
            self.list[index].append([tuple([key, value])])
        else:
            self.list[index] = [tuple([key, value])]
        self.occupied += 1

    # def __repr__(self):
    #     return []
