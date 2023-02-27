from datetime import datetime
import subprocess
# tutaj ustawiamy przedział czasu w którym chcemy otworzyć nasz notatnik
scheduled_time_earlier = datetime(2023, 1, 19, 19, 39, 10, 1000)
scheduled_time_later = datetime(2023, 1, 19, 19, 40, 10, 1000)
present_time = datetime.now()

while True:
    present_time = datetime.now()
    # Notatnik otworzy jeśli czas teraz jest w przedziale między czasem wcześniejszym a czasem późniejszym przez
    # nas zdefiniowanym wyżej
    if scheduled_time_earlier < present_time < scheduled_time_later:
        subprocess.Popen("notepad.exe")
        break
