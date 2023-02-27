# Script that deletes moves or copies a file

from os import remove
from shutil import move, copy


def move_file():
    old_file = input("Podaj miejsce zrodlowe pliku")
    destination = input("Podaj miejsce docelowe pliku")
    try:
        move(old_file, destination)
    except FileNotFoundError:
        print("Plik lub miejsce docelowe nie istnieje")


def copy_file():
    old_file = input("Podaj miejsce zrodlowe pliku")
    destination = input("Podaj miejsce docelowe pliku")
    try:
        copy(old_file, destination)
    except FileNotFoundError:
        print("Plik lub miejsce docelowe nie istnieje")


def delete_file():
    old_file = input("Podaj miejsce zrodlowe pliku do usuniecia")
    try:
        remove(old_file)
    except FileNotFoundError:
        print("Taki plik nie istnieje istnieje")
    return


user_input = ""
validate = True
while validate:
    try:
        user_input = int(input("Ktora operacje chcesz wykonac 1 dla przeniesienia 2 dla skopiowania 3 dla usuniecia"))
        validate = False
    except ValueError:
        print("Podaj poprawna liczbe")
        validate = True
while 0 < user_input < 4:
    if user_input == 1:
        move_file()
        break
    elif user_input == 2:
        copy_file()
        break
    elif user_input == 3:
        delete_file()
        break
    else:
        print("Wybierz poprawna liczbe")
