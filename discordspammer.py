import pyautogui as py 
import sys
import time as ti
import keyboard as key
from colorama import init, Fore
init(autoreset=True)
fast_or_slow = None
def fast_mode():
    for _ in range(How_many_times_do_you_want_to_spam):
        py.write(what_word_to_SPAM)
        ti.sleep(intkey)
        #very tiny hard coded break just so it picks it up
        ti.sleep(0.1)
        py.press("enter")
def slow_mode():
    for _ in range(How_many_times_do_you_want_to_spam):
        py.write(what_word_to_SPAM, interval=0.1)
        ti.sleep(intkey)
        #very tiny hard coded break just so it picks it up
        ti.sleep(0.1)
        py.press("enter")
def clear():
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()
what_word_to_SPAM = input("what word would you like to spam:")
while what_word_to_SPAM == "":
    clear()
    print(Fore.RED + "this can't be null")
    what_word_to_SPAM = input("what word would you like to spam:")
How_many_times_do_you_want_to_spam = int(input("how many times would you like to spam:"))
clear()
intkey = float(input("interval between key press:"))
clear()
f_or_slow = input("fast or slow mode? f/s:")
if f_or_slow == "f":
    fast_or_slow = True
elif f_or_slow == "s":
    fast_or_slow = False
if fast_or_slow:
    print("press s to start")
    key.wait("s")
    py.press("backspace")
    fast_mode()
else:
    print("press s to start")
    key.wait("s")
    py.press("backspace")
    slow_mode()
