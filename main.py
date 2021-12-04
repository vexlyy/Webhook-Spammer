# imports
import os
import time
import platform
from tkinter import messagebox
import webbrowser
import sys
import requests

# Colors
Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"

os.system("cls")
print(f"""

{Red}                         ██╗   ██╗███████╗██╗  ██╗██╗  ██╗   ██╗  {Reset}          ┌─────────────────────────────────────────────┐
{Red}                         ██║   ██║██╔════╝╚██╗██╔╝██║  ╚██╗ ██╔╝  {Reset}          │  1.                                           │
{Red}                         ██║   ██║█████╗   ╚███╔╝ ██║   ╚████╔╝   {Reset}          │                                             │
{Red}                         ╚██╗ ██╔╝██╔══╝   ██╔██╗ ██║    ╚██╔╝   {Reset}           │                                             │      
{Red}                          ╚████╔╝ ███████╗██╔╝ ██╗███████╗██║     {Reset}          │                                             │
{Red}                           ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     {Reset}          └─────────────────────────────────────────────┘

                        {Yellow}          discord.gg/chairs {Reset}
                                       

""")

Url = input(f"{Yellow}Webhook URL : ")

Text = input("What Text do you want to spam? : ")

while True:
    mUrl = Url

    data = {"content": Text}
    response = requests.post(mUrl, json=data)

    print("Sent")





