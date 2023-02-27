from random import randrange
# Script that checks if you guessed the right number that was randomly generated

def input_check():
    try:
        int(user_number)
    except ValueError:
        return False
    if int(user_number) > 20 or int(user_number) < 1:
        return False
    return True


should_continue = True
num = randrange(1, 20, 1)
while should_continue:
    user_number = input("Podaj numer od 1 do 20")
    while not input_check():
        user_number = input("Podaj poprawna liczbe od 1 do 20")

    if num == int(user_number):
        print("Zgadles")
        should_continue = False
    else:
        print("Nie zgadles")
        should_continue = True

    
