import csv
import re


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for file_name in file_list:
        with open(file_name, encoding='cp1251') as f_n:
            for row in f_n:
                param = re.split(":\s+", row.strip())
                if isinstance(param, list) and len(param) == 2:
                    if param[0] == 'Изготовитель системы':
                        os_prod_list.append(param[1])
                    elif param[0] == 'Название ОС':
                        os_name_list.append(param[1])
                    elif param[0] == 'Код продукта':
                        os_code_list.append(param[1])
                    elif param[0] == 'Тип системы':
                        os_type_list.append(param[1])
    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    return header, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv(out_file):
    """Запись данных в csv"""

    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report.csv')
