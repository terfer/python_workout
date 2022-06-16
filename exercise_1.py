from random import randint

def input_generator(try_number : bool) -> int:
    if try_number:
        print("Introduce un número del 0 al 100 incluidos:")
    else:
        print("Vuelve a intentarlo")
    return int(input())

def guessing_game():
    machine_number = randint(0,100)
    user_number = input_generator(True)
    while machine_number != user_number:        
        if machine_number > user_number:
            print("Demasiado bajo")
            user_number = input_generator(False)
        else:
            print("Demasiado alto")
            user_number = input_generator(False)
    return print("Correcto")

guessing_game()