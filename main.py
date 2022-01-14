import TsDIct

if __name__ == '__main__':
    di = TsDIct.TsDict()
    di.put(1, 2)
    di.put(1, 2)
    di.put(8, 3)
    di.put(2, 3)
    di.put('1', 3)
    di.put(4, 3)
    di.put('2', 3)
    di.put('alice', 3)

    di.put(1, ['ali', 'jason'])
    print(di.list)
    print(di)
    a = dict()
    a['1'] = 2
    print(a)
    a['1'] = 3
    a[1] = 3
    a[5] = 3

    print(a)
