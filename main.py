import TsDIct
import concurrent.futures

if __name__ == '__main__':
    dictionary = TsDIct.TsDict()
    # di.put(1, 2)
    # di.put(1, 2)
    # di.put(8, 3)
    # di.put(2, 3)
    # di.put('1', 3)
    # di.put(4, 3)
    # di.put('2', 3)
    # di.put('alice', 3)
    # print(di.get('alice'))
    # print(di.get('2'))
    # print(di.get('8'))
    # print(di.get(8))
    # print(di.get(1))
    #
    # di.put(1, ['ali', 'jason'])
    # print(di.get(1))
    # print(di.key_set())
    #
    # print(di.list)
    # print(di)
    # print(di.remove('alice'))
    # print(di.list)
    # print(di)
    #
    # a = dict()
    # a['1'] = 2
    # print(a)
    # a['1'] = 3
    # a[1] = 3
    # a[5] = 3
    # print(a)
    with open("EnglishPersianWordDatabase.txt", 'r', encoding='utf-8') as file:
        text = file.read().replace('-', '').replace('\n', '').split('|')
    stripped = [s.strip() for s in text if s != '']
    del stripped[0]
    keys = stripped[1::2]
    values = stripped[0::2]

    # for i in range(0,50):
    #     dictionary.put(keys[i],values[i])
    # print(dictionary)

    with concurrent.futures.ThreadPoolExecutor(25) as executor:
        for i in range(0, len(keys)):
            executor.submit(dictionary.put, keys[i], values[i])
            print(keys[i] + ' : ' + values[i])

    print(dictionary.get('همزاد'))
    print(dictionary.occupied)
    print(len(keys))
    print(len(values))
