import os, time, requests, colorama
from colorama import Fore, Style
from threading import Thread
from datetime import datetime
os.system("cls")

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
f  = open("Main/text.txt","r",encoding="utf8")
ascii = "".join(f.readlines())
print(colorText(ascii))
time.sleep(3)
os.system("py Main/COOKIES.py")