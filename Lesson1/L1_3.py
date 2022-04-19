'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.'''

word1 = b"attribute"
#т.к без перекодирования кирилицу нельзя записать в байтовом типе, то делаем encode
word2 = "класс".encode('utf-8')
word3 = "функция".encode('utf-8')
word4 = b"type"

print(word1, word2, word3, word4)
