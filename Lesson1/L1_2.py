'''Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.'''

word1 = b"class"
word2 = b"function"
word3 = b"method"

print(type(word1), type(word2), type(word3))

print(word1, word2, word3)

print(len(word1), len(word2), len(word3))
