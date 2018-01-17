import re


def get_password_strength(password):
    return empty_password(password) + \
        check_length_password(password) + \
        check_letters_password(password) + \
        check_numbers_password(password) + \
        check_lower_and_upper(password) + \
        check_blacklist_password(password) + \
        symbols_password(password)


def empty_password(password):
    return 1 if password else 0


def check_length_password(password):
    before_eight = 1 if len(password) > 7 else 0
    after_fourty = 1 if len(password) < 41 else 0
    return before_eight + after_fourty


def check_letters_password(password):
    return 1 if re.findall(r'[a-zA-Z]+', password) else 0


def check_numbers_password(password):
    return 1 if re.findall(r'\d+', password) else 0


def check_lower_and_upper(password):
    lower_letters = 1 if re.findall(r'[a-z]+', password) else 0
    upper_letters = 1 if re.findall(r'[A-Z]+', password) else 0
    return lower_letters + upper_letters


def check_blacklist_password(password):
    blacklist = ["123456", "qwerty", "drop table user", ""d]
    return 0 if password in blacklist else 1


def symbols_password(password):
    special_symbols = re.compile("[#@$]")
    find_special_symbols = re.findall(special_symbols, password)
    find_all_symbols = re.findall(r"\W+", password)
    if find_special_symbols == find_all_symbols:
        return 2
    elif find_special_symbols:
        return 1
    else:
        return 0


if __name__ == '__main__':
    password = ''
    print(
        get_password_strength(password)
    )
