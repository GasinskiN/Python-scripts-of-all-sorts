import subprocess
import pyautogui
import time


subprocess.Popen(["notepad.exe"])
time.sleep(3)
pyautogui.typewrite("test1@test.com, P@ssword1!\ntest2@test.com, P@ssword2!\n\ntest3@test.com, P@ssword3!")
time.sleep(2)
pyautogui.click(1100, 15)