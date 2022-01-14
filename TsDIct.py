import threading


class TsDict:
    lock = threading.Lock()

    def __init__(self):
        self.size = 10
        self.occupied = 0
        self.max_bucket_length = 0
        self.list = [list() for _ in range(10)]

    def __find_index__(self, key):
        match str(type(key)):

            case "<class 'str'>":
                sum_ord = 0
                for letter in key:
                    sum_ord += ord(letter)
                return sum_ord % len(self.list)

            case "<class 'int'>":
                return key % len(self.list)

            case "<class 'float'>":
                sum_ord = 0
                for letter in str(key):
                    sum_ord += ord(letter)
                return sum_ord % len(self.list)

            case "<class 'list'>":
                sum_ord = 0
                for i in key:
                    sum_ord += ord(str(i))
                return sum_ord % len(self.list)

            case _:
                return None

    def __rehash__(self):
        if 0.75 * len(self.list) <= self.occupied or self.max_bucket_length >= 10:
            self.list.extend([list() for _ in range(len(self.list) * 2)])
            for element in self.list:
                if len(element) != 0:
                    self.put(element[0], element[1])

    def put(self, key, value):
        self.__rehash__()
        index = self.__find_index__(key)
        if len(self.list[index]) != 0:
            for i in range(0, len(self.list[index])):
                if self.list[index][i][0] == key:
                    self.list[index][i] = tuple([self.list[index][i][0], value])
                    return
            self.list[index].append(tuple([key, value]))
        else:
            self.list[index] = [tuple([key, value])]
        self.occupied += 1
        if len(self.list[index]) > self.max_bucket_length:
            self.max_bucket_length = len(self.list[index])

    def __repr__(self):
        out = '{'
        for i in range(0, len(self.list)):
            if len(self.list[i]) > 0:
                for j in range(0, len(self.list[i])):
                    if len(self.list[i][j]) > 0:
                        key = f"'{self.list[i][j][0]}'" if type(self.list[i][j][0]) is str else self.list[i][j][0]
                        val = f"'{self.list[i][j][1]}'" if type(self.list[i][j][1]) is str else self.list[i][j][1]
                        out += f'{key}: {val}, '

        return out[:-2] + '}'
