import requests
from colorama import Fore, Style, init
import os
import toreadable

url = "http://localhost:5000"
if os.name == "nt":
    init(convert=True, autoreset=True)
else:
    init(convert=False, autoreset=True)


def print_trie(trie, depth):
    if trie == {}:
        return
    if isinstance(trie, str):
        for x in range(depth):
            print(f"{Fore.BLUE} ", end="")
        print(f"{Fore.BLUE}{trie}")
        return

    for (key, value) in trie.items():
        for x in range(depth):
            print(" ", end="")
        print(f"{Fore.BLUE}{key}")
        print_trie(value, depth + 1)


while True:
    page = f"""
    {Fore.MAGENTA}1. {Fore.CYAN}Add a word to the trie
    {Fore.MAGENTA}2. {Fore.CYAN}Remove a word from the trie
    {Fore.MAGENTA}3. {Fore.CYAN}Search for a word in the trie
    {Fore.MAGENTA}4. {Fore.CYAN}Prefix keyword autocompletion
    {Fore.MAGENTA}5. {Fore.CYAN}Display the trie
    {Fore.MAGENTA}6. {Fore.CYAN}Display all the words in the trie
    {Fore.MAGENTA}7. {Fore.CYAN}Clear the trie
    {Fore.MAGENTA}8. {Fore.CYAN}Exit
    """
    os.system("cls")
    print(page)
    c = input(f"{Fore.YELLOW}Enter your choice: ")
    # check if c is a integer
    if not c.isdigit():
        input(f"{Fore.RED}Please enter a number (press enter to continue)")
        continue
    if int(c) == 1:
        word = input(f"{Fore.YELLOW}Enter the word you want to add: ").lower()
        r = requests.get(f"{url}/add/{word}")
        if r.status_code == 200:
            input(f"{Fore.GREEN}Word added successfully (press enter to continue)")
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 2:
        word = input(f"{Fore.YELLOW}Enter the word you want to remove: ").lower()
        r = requests.get(f"{url}/remove/{word}")
        if r.status_code == 200:
            input(f"{Fore.GREEN}Word removed successfully (press enter to continue)")
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 3:
        word = input(f"{Fore.YELLOW}Enter the word you want to search for: ").lower()
        r = requests.get(f"{url}/search/{word}")
        if r.status_code == 200:
            if r.json()["Status"] == True:
                input(f"{Fore.GREEN}Word found (press enter to continue)")
            else:
                input(f"{Fore.RED}Word not found (press enter to continue)")
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 4:
        word = input(f"{Fore.YELLOW}Enter the prefix you want to search for: ").lower()
        r = requests.get(f"{url}/suggest/{word}")
        if r.status_code == 200 and r.json() != []:
            r = r.json()
            for i in r["Status"]:
                print(f"{Fore.BLUE}{i}")
            input(f"{Fore.GREEN}Suggestions found (press enter to continue)")

        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 5:
        r = requests.get(f"{url}/struct")

        if r.status_code == 200:
            c = input(
                f"{Fore.YELLOW}Print as dict (1), Print as list by depth (2) ASCII output, not recomended for large trie. (3):  "
            )
            if int(c) == 1:
                send = trie = r.json()["trie"]
                print(f"{Fore.BLUE}{send}", 0)
            elif int(c) == 2:
                trie = toreadable.export((r.json()["trie"]))
                print(f"{Fore.BLUE}{trie}")
            elif int(c) == 3:
                print("\n")
                print_trie(r.json()["trie"], 0)
                print("\n")
            input(f"{Fore.GREEN}Trie displayed successfully (press enter to continue)")
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 6:
        r = requests.get(f"{url}/words")
        if r.status_code == 200:
            print(f"{Fore.GREEN}{r.json()['words']}")
            input(
                f"{Fore.GREEN}All words displayed successfully (press enter to continue)"
            )
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 7:
        r = requests.get(f"{url}/clear")
        if r.status_code == 200:
            input(f"{Fore.GREEN}Trie cleared successfully (press enter to continue)")
        else:
            input(f"{Fore.RED}Error: {r.json()['Error']} (press enter to continue)")
    elif int(c) == 8:
        exit("Exiting...")
