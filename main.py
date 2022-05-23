import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def chars_generator(cond_digits, cond_lower_case, cond_upper_case, cond_symbols):
    chrs = ''
    if cond_digits == 'да':
        chrs += digits
    if cond_lower_case == 'да':
        chrs += lowercase_letters
    if cond_upper_case == 'да':
        chrs += uppercase_letters
    if cond_symbols == 'да':
        chrs += punctuation
    return chrs


def password_generator(lengt, chrs):
    password = ''
    for i in range(lengt):
        password += random.choice(chrs)
    return password


while True:
    number_of_pass = int(input('Сколько паролей нужно сгенерировать?\n'))
    len_password = int(input('Какой длинны должен быть один пароль?\n'))
    add_digits = input('Включать в пароль цифры? (да / нет)\n')
    add_lower_case = input('Включать в пароль прописные буквы? (да / нет)\n')
    add_upper_case = input('Включать в пароль строчные буквы? (да / нет)\n')
    add_symbols = input('Включать в пароль символы (!#$%&*+-=?@^_)? (да / нет)\n')

    chars = chars_generator(add_digits, add_lower_case, add_upper_case, add_symbols)

    for i in range(number_of_pass):
        print(password_generator(len_password, chars))
    if input('Сгенерировать еще пароли? (да, нет)') == 'да':
        continue
    else:
        print('Пользуйтесь наздоровье, досвидания!')
        break
