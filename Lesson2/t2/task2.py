import json


def write_order_to_json(item, quantity, price, buyer, date):
    """Запись в json"""

    with open('orders_1.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders_1.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)


write_order_to_json('PC', 5, 50, 'sana9056', '2022-04-01')
write_order_to_json('BOOK', 4, 40, 'delexi', '2022-04-02')
write_order_to_json('Scaner', 3, 30, 'i4kra', '2022-04-03')
write_order_to_json('apple', 2, 20, 'Memfis', '2022-04-04')
write_order_to_json('geekbrains', 1, 10, 'Monty', '2022-04-05')
