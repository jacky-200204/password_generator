#password generator
from random import choice

def gen_strong_password(num, length=10):
    words = ['A', 'X', 'Y', 'K', 'H', 'C', 'Z', 'a', 'x', 'n', 'B', 'C', 'F', '1', 'q', 'e', '3', 'U', 'T', '#', '-', '@']
    passwords = []
    for i in range(num):
        password_list = [choice(words) for i in range(length)]
        passwords.append(''.join(password_list))

    return passwords

def gen_week_password(num, length=6):
    word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'o', 'u']
    passwords = []
    for i in range(num):
        password = [choice(word_list) for i in range(length)]
        passwords.append(''.join(password))

    return passwords

def take_input(msg, find_in=None):
    while True:
        print(msg)
        response = input(":> ").lower().strip()
        try:
            n_or_s = int(find_in)
        except ValueError:
            if response not in find_in or response == '':
                continue
            else:
                break
        else:
            try:
                response = int(response)
            except ValueError:
                continue
            else:
                break
    # try:
    #     response = int(response)
    # except ValueError:
    #     pass
    return response

num_str = "1234567890"
strong_week_msg = "Do you want to generate strong or week password? (S/W)"
strong_num_msg = "How many strong password do you want?"
week_num_msg = "How many week password do you want?"

response = take_input(strong_week_msg, 'sw')
if response == 's':
    numbers = take_input(strong_num_msg, num_str)
    strong_password = gen_strong_password(numbers, 10)
    for x in strong_password:
        print(x)
else:
    number = take_input(week_num_msg, num_str)
    week_password = gen_week_password(number)
    for i in week_password:
        print(i)
