import pyautogui
import time
import sys

a = input("Choose Spam: "
          "[1]Bee_Movie "
          "[2]Baby-Justin_Be-beer ")

print("10")
time.sleep(1)
print("9")
time.sleep(1)
print("8")
time.sleep(1)
print("7")
time.sleep(1)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Spamming...Press CTRL + C in this window to Stop everything")


if a == "1":
    wrd = open("Texts Files/bees", 'r')
    for word in wrd:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
else:
    if a == "2":
        wrd = open("Texts Files/baby", 'r')
        for word in wrd:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
print("Finished")
