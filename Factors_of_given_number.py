#Script that gives you the factors of a number specified by input
def input_check():
    try:
        int(input_number)
    except ValueError:
        return False
    if int(input_number) > 100 or int(input_number) < 1:
        return False
    return True


input_number = input("podaj liczbe od 1 do 100")
while not input_check():
    input_number = input("podaj poprawna liczbe od 1 do 100")
array_of_factors = []
for x in range(1, int(input_number)):
    if int(input_number) % x == 0:
        array_of_factors.append(x)

array_of_factors.sort(reverse=True)
print(array_of_factors)

        
    
