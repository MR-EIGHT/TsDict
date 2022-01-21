import TsDIct
import concurrent.futures

if __name__ == '__main__':
    FaEn_dictionary = TsDIct.TsDict()
    EnFa_dictionary = TsDIct.TsDict()

    with open("EnglishPersianWordDatabase.txt", 'r', encoding='utf-8') as file:
        text = file.read().replace('-', '').replace('\n', '').split('|')
    stripped = [s.strip() for s in text if s != '']
    del stripped[0]
    persian_words = stripped[1::2]
    english_words = stripped[0::2]

    with concurrent.futures.ThreadPoolExecutor(25) as executor:
        executor.map(FaEn_dictionary.put, persian_words[:], english_words[:])
        executor.map(EnFa_dictionary.put, english_words[:], persian_words[:])

        # for i in range(35537, len(persian_words)):
        #     executor.submit(dictionary.put, persian_words[i], english_words[i])

    print(FaEn_dictionary.get('همزاد'))
    print(FaEn_dictionary.get('کوشش کردن'))
    print(FaEn_dictionary.get('تثليث'))
    print(FaEn_dictionary.get('سه راه'))

    print(EnFa_dictionary.get('twin'))
    print(EnFa_dictionary.get('try'))
    print(EnFa_dictionary.get('trinity'))
    print(EnFa_dictionary.get('triode'))

    print(FaEn_dictionary.occupied)
    print(EnFa_dictionary.occupied)

    print(len(persian_words))
    print(len(english_words))
