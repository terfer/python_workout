from random import choice


def create_password_generator(dictionary: str):
    def len_of_password(n: int):
        password = ""
        while len(password) < n:
            password += choice(dictionary)
        return password
    return len_of_password


alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')
 
print(alpha_password(5))
print(alpha_password(10))
 
print(symbol_password(5))
print(symbol_password(10))
