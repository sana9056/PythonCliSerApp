'''Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).'''#done

word1 = "разработка".encode('utf-8')
word2 = "администрирование".encode('utf-8')
word3 = "protocol".encode('utf-8')
word4 = "standard".encode('utf-8')

print(word1, word2, word3, word4)

word1 = word1.decode('utf-8')
word2 = word2.decode('utf-8')
word3 = word3.decode('utf-8')
word4 = word4.decode('utf-8')

print(word1, word2, word3, word4)
