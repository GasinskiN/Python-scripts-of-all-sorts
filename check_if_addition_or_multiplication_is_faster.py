import time

start_time = time.perf_counter()

sum = 0
for i in range(1,31):
    for j in range(1, 31):
        temp = j + i

end_time = time.perf_counter()
add_time = end_time - start_time

start_time = time.perf_counter()

product = 1
for i in range(1, 31):
    for j in range(1, 31):
        temp = i * j

end_time = time.perf_counter()
mult_time = end_time - start_time

print("czas dodawania:", add_time)
print("czas mnożenia:", mult_time)

if add_time > mult_time:
    print("Mnożenie szybsze")
else:
    print("Dodawanie szybsze")
