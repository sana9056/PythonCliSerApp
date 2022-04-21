'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.'''

word1 = b"attribute"

    #word2 = b"класс"
    #print(word2)
    #SyntaxError: bytes can only contain ASCII literal characters
    #word3 = b"функция"
    #print(word3)
    #SyntaxError: bytes can only contain ASCII literal characters

#т.к без перекодирования кирилицу нельзя записать в байтовом типе, то делаем encode
word2 = "класс".encode('utf-8') #b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'
word3 = "функция".encode('utf-8') #b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
word4 = b"type"

print(word1, word2, word3, word4)
