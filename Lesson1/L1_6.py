'''Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.'''

from chardet import detect

LIST = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for line in LIST:
        file.write(f'{line}\n')
file.close()


def encoding_convert():
    with open('test.txt', 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open('test.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


encoding_convert()

with open('test.txt', 'r', encoding='utf-8') as file:
    CONTENT = file.read()
print(CONTENT)
