from getpass import getpass as wait
from time import sleep
import os

def clear(waitingTime):
    sleep(waitingTime)
    print("...")
    wait("")
    os.system("cls")