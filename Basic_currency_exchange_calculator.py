# A basic currency exchange calculator

def selection_check(given_number):
    try:
        int(given_number)
    except ValueError:
        return False
    if int(given_number) == 1 or int(given_number) == 2 or int(given_number) == 3:
        return True
    return False


def input_check(user_number):
    try:
        float(user_number)
    except ValueError:
        return False
    if float(user_number) <= 0:
        return False
    return True


euro = 1.00
dollar = 1.11
bolivar = 0.00001
type_of_currency_had = input("Wpisz posiadana walute, 1 - euro 2 - dolar 3 - boliwar wenezuelski")

while not selection_check(type_of_currency_had):
    type_of_currency_had = input("Podaj poprawna liczbe 1 - euro 2 - dolar 3 - boliwar wenezuelski")

amount_of_currency_had = input("Podaj jaka ilosc waluty chcesz przekonwertowac")

while not input_check(amount_of_currency_had):
    amount_of_currency_had = input("Podaj nieujemna liczbe")

stndrt_value = 0
if int(type_of_currency_had) == 1:
    stndrt_value = float(amount_of_currency_had)
elif int(type_of_currency_had) == 2:
    stndrt_value = float(amount_of_currency_had) * dollar
elif int(type_of_currency_had) == 3:
    stndrt_value = float(amount_of_currency_had) * bolivar

type_of_currency_to_convert_to = input("Na jaka walute chcesz zamienic 1 - euro 2 - dolar 3 - boliwar wenezuelski")

while not selection_check(type_of_currency_to_convert_to) or type_of_currency_had == type_of_currency_to_convert_to:
    type_of_currency_to_convert_to = input("Podaj liczbe od 1 do 3 inna niz poprzednio wybrana")

converted_amount = 0
if int(type_of_currency_to_convert_to) == 1:
    converted_amount = "Po konwercji jest to " + str(stndrt_value) + "euro"
elif int(type_of_currency_to_convert_to) == 2:
    converted_amount = "Po konwercji jest to " + str(float(stndrt_value) / dollar) + "dolarow"
elif int(type_of_currency_to_convert_to) == 3:
    converted_amount = "Po konwercji jest to " + str(float(stndrt_value) / bolivar) + " Boliwarow wenezuelskich"
print(converted_amount)
