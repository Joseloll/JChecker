import time
import os
import colorama
from colorama import Fore
import requests
os.system(f'cls & mode 85,20 & title JSpammer!')

def main():
    menu()


def menu():
    choice = input(Fore.LIGHTRED_EX+ """
         __________              __            
      / / ____/ /_  ___  _____/ /_____  _____
 __  / / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
/ /_/ / /___/ / / /  __/ /__/ ,< /  __/ /    
\____/\____/_/ /_/\___/\___/_/|_|\___/_/                                                                                                                 
                Made By Jose#0001                             
                [1]  Discord Vanity Checker
                [2]  Multi Vanity Checker 
                Enter Your Choice ↓
                """)
    if choice == "1":
        checker()
    elif choice == '2':
        checkers()
    else:
        print("Enter Right Choice")
        time.sleep(3)
        os.system('cls')
        menu()



def checker():
    print(Fore.YELLOW + "Put A Single Word And Not discord.gg/{your vanity you wanna check}")
    url = input(Fore.LIGHTRED_EX + 'Enter Your Discord Vanity Url:')
    r = requests.get(f"https://discordapp.com/api/invites/{url}")
    if r.status_code == 404:
        print(Fore.GREEN + "Discord Vanity Is Not Taken")
        time.sleep(2)
        os.system('cls')
        menu()

    else:
        print(Fore.RED + "Discord Vanity Is Taken")
        time.sleep(2)
        os.system('cls')
        menu()




def checkers():
    print(Fore.YELLOW + "This Checks Multi Vanity At One Time")
    name = input(Fore.LIGHTRED_EX + "Enter The Name Of The Txt File:")
    file = open(name, "r").read().split('\n')
    for check in file:
        r = requests.get(f'https://discord.com/api/v9/invites/{check}')
        if r.status_code == 404:
            print(Fore.GREEN + f'{check} Is Valid')
            time.sleep(1)
        else:
            print(Fore.RED + f'{check} Is Invalid')
            time.sleep(1)
           

main()