import TsDIct
import concurrent.futures

if __name__ == '__main__':
    dictionary = TsDIct.TsDict()

    with open("EnglishPersianWordDatabase.txt", 'r', encoding='utf-8') as file:
        text = file.read().replace('-', '').replace('\n', '').split('|')
    stripped = [s.strip() for s in text if s != '']
    del stripped[0]
    keys = stripped[1::2]
    values = stripped[0::2]

    with concurrent.futures.ThreadPoolExecutor(25) as executor:
        for i in range(0, len(keys)):
            executor.submit(dictionary.put, keys[i], values[i])
            # print(keys[i] + ' : ' + values[i])

    print(dictionary.get('همزاد'))
    print(dictionary.get('کوشش کردن'))
    print(dictionary.get('تثليث'))
    print(dictionary.get('سه راه'))

    print(dictionary.occupied)
    print(len(keys))
    print(len(values))
