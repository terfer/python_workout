def menu(**kwargs):
    while True:
        option = '/'.join(sorted(kwargs))
        choice = input(f"Enter a option {option}: ")
        if choice in kwargs:
            return kwargs['choice']()

if __name__ == '__main__':
    menu()