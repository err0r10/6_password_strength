import re
import sys
from os.path import exists


def load_data(filepath):
    with open(filepath) as password_file:
        return password_file.read().split("\n")


def get_password_strength(login, password):
    special_symbols = "#@$"
    return [
             sum ([
                check_empty_password(password),
                check_length_password(password),
                check_numbers_password(password),
                check_lower_and_upper(password),
                check_blacklist_password(password),
                check_spec_symbols_password(password, special_symbols),
                check_other_symbol(password, special_symbols),
                check_password_login(login, password)
             ])
    ]


def check_empty_password(password):
    return len(password) > 0


def check_length_password(password):
    min_size = 7
    max_size = 41
    return len(password) > min_size and len(password) < max_size


def check_numbers_password(password):
    return len(re.findall(r'\d+', password)) > 0


def check_lower_and_upper(password):
    lower_letters = len(re.findall(r'[a-z]+', password)) > 0
    upper_letters = len(re.findall(r'[A-Z]+', password)) > 0
    return lower_letters + upper_letters


def check_blacklist_password(password):
    blacklist_password = ["123456", "qwerty", "drop table user", ""]
    return password not in blacklist_password


def check_spec_symbols_password(password, special_symbols):
    find_special_symbols = [
        symbol for symbol in special_symbols if symbol in password
    ]
    return len(find_special_symbols) > 0


def check_other_symbol(password, special_symbols):
    find_all_symbols = re.findall(r"\W+", password)
    string_all_symbol = ''.join(find_all_symbols)
    return all(s in set(special_symbols) for s in set(string_all_symbol))


def check_password_login(login, password):
    return login not in password


if __name__ == '__main__':
    if len(sys.argv) != 2 or not exists(sys.argv[1]):
        sys.exit("The file doesn't exist!")
    file_path = sys.argv[1]
    accounts = load_data(file_path)
    for account in accounts:
        login, password = account.split(",")
        print(get_password_strength(login, password))
