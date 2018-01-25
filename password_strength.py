import re


def get_password_strength(password):
    return


def empty_password(password):
    return len(password) > 0


def check_length_password(password):
    min_size_password = 7
    max_size_password = 41
    before_eight = len(password) > min_size_password
    after_fourty = len(password) < max_size_password
    return before_eight + after_fourty


def check_numbers_password(password):
    return re.findall(r'\d+', password) > 0


def check_lower_and_upper(password):
    lower_letters = re.findall(r'[a-z]+', password) > 0
    upper_letters = re.findall(r'[A-Z]+', password) > 0
    return lower_letters + upper_letters


def check_blacklist_password(password):
    blacklist = ["123456", "qwerty", "drop table user", ""]
    return password in blacklist


def symbols_password(password):
    special_symbols = re.compile("[#@$]")
    find_special_symbols = re.findall(special_symbols, password)
    find_all_symbols = re.findall(r"\W+", password)


if __name__ == '__main__':
    password = ''
    print(
        get_password_strength(password)
    )
