'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.'''

list = ['attribute', 'класс', 'класс']

for i in list:
    try:
        print(i.encode(encoding='ascii'))
    except Exception as e:
        print(f'Невозможно записать в байтовом типе: {e}')
        print(i.encode('utf8'))
