import sys
import json
import socket
import time
import argparse
import logging
import log.client_log_config
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, DEFAULT_PORT, ERROR, DEFAULT_IP_ADDRESS
from common.utils import get_message, send_message
from decos import log


CLIENT_LOGGER = logging.getLogger('client')


@log
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def process_ans(message):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : ACCEPTED'
        return f'400 : {message[ERROR]}'
    raise ValueError


@log
def create_arg_parser():
    """
    Создаём парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
            f' Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    CLIENT_LOGGER.info(f'Запущен клиент с парамертами: '
                       f'адрес сервера: {server_address}, порт: {server_port}')

    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
