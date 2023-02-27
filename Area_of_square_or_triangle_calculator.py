# Script that calculates the area of a triangle or square
def input_check(user_number):
    try:
        float(user_number)
    except ValueError:
        return False
    if float(user_number) <= 0:
        return False
    return True


def selection_check(given_number):
    try:
        int(given_number)
    except ValueError:
        return False
    if int(given_number) == 1 or int(given_number) == 2:
        return True
    return False


square_or_triangle = input("Podaj 1 dla trojkata 2 dla kwadratu")

while not selection_check(square_or_triangle):
    square_or_triangle = input("Podaj poprawna liczbe 1 lub 2")

if int(square_or_triangle) == 1:
    triangle_height = input("Podaj wysokosc trojkata")

    while not input_check(triangle_height):
        triangle_height = input("Podaj dodatnia liczbe calkowita do 100000")

    triangle_base = input("Podaj podstawe trojkata")

    while not input_check(triangle_base):
        triangle_base = input("Podaj dodatnia liczbe calkowita do 100000")

    print("Trojkat ma pole " + str(float(triangle_height) * float(triangle_base)/2))
elif int(square_or_triangle) == 2:
    first_side = input("podaj pierwszy bok")

    while not input_check(first_side):
        first_side = input("Podaj dodatnia liczbe calkowita do 100000")

    second_side = input("podaj drugi bok")

    while not input_check(second_side):
        second_side = input("Podaj dodatnia liczbe calkowita")

    print("Kwadrat ma Pole " + str(float(first_side) * float(second_side)))
