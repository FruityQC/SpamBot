import pyautogui
import time
import sys
import os


def start():

    os.system("cls")

    user = input("Choose Spam: "
            "[1]Bee_Movie "
            "[2]Baby-Justin_Be-beer ")

    if user != '1' and user != '2': 
        print('[' + user + ']' + " Is an INVALID Input")
        time.sleep(5)
        start()

    number = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for x in number:
        print(x)
        time.sleep(1)

    print("Spamming...Press CTRL + C in this window to Stop everything")


    if user == "1":
        wrd = open("SpamBot-main/bees", 'r')
        for word in wrd:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    else:
        if user == "2":
            wrd = open("SpamBot-main/baby", 'r')
            for word in wrd:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
    print("Finished")

start()