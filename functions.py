from getpass import getpass as wait
from time import sleep
import os

def clear(waitingTime:float):
    sleep(waitingTime)
    print("...")
    wait("")
    os.system("cls")

def choice(tuple_options:tuple, count:tuple=("[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]", "[H]", "[I]")):
    print("What do I choose:")
    list_options = [f"   {count[i]} {v}" for i, v in enumerate(tuple_options)]
    options = "\n".join(list_options)
    print(options)
    answere = input("\n")
    sleep(.5)
    if answere in [list_options[i][4].lower() for i, n in enumerate(tuple_options)]:
        return answere
    else:
        return 0

def dialogue(lines:list):
    print("\n".join(lines))
    sleep(.5)
