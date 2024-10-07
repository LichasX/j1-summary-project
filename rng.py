import random
import time
from colorama import Fore, Style


def rng_generator():
    x = random.randint(1, 1000000)
    return x


def rng_game():
    x = rng_generator()
    if x > 500000:
        return f"{Style.RESET_ALL}Common (1 in 2)"
    elif 500000 >= x > 250000:
        return f"{Fore.GREEN}{Style.NORMAL}Uncommon (1 in 4)"
    elif 250000 >= x > 125000:
        return f"{Fore.BLUE}{Style.NORMAL}Rare (1 in 8)"
    elif 125000 >= x > 62500:
        return f"{Fore.BLUE}{Style.BRIGHT}Super Rare! (1 in 16)"
    elif 62500 >= x > 31250:
        return f"{Fore.MAGENTA}{Style.NORMAL}Epic! (1 in 32)"
    elif 31250 >= x > 15625:
        return f"{Fore.YELLOW}{Style.NORMAL}Lengendary! (1 in 64)"
    elif 15625 >= x > 5625:
        return f"{Fore.RED}{Style.NORMAL}Mythic!! (1 in 100)"
    elif 5625 >= x > 625:
        return f"{Fore.WHITE}{Style.BRIGHT}Marvellous!! (1 in 200)"
    elif 625 >= x > 125:
        return f"{Fore.WHITE}{Style.DIM}Secret!! (1 in 2000)"
    elif 125 >= x > 25:
        return f"{Fore.BLACK}{Style.BRIGHT}UNBELIVABLE!!! (1 in 10000)"
    elif 25 >= x > 1:
        return f"{Fore.GREEN}{Style.BRIGHT}INCOMPREHENSIBLE!!!! (1 in 40000)"
    elif x == 1:
        return f"{Fore.YELLOW}{Style.BRIGHT}JACKPOT!!!!!!! (1 in 1000000)"


def loading_percentage():
    percentage = 0
    while percentage < 100:
        x = random.randint(1, 10)
        percentage = percentage + x
        if percentage > 100:
            percentage = 100
        print(f"Loading... ({percentage}% done)", end="\r")
        time.sleep(0.5)
    time.sleep(1)
    print("Complete!!")


def proceeding():
    loading = [".", "..", "..."]
    for i in range(21):
        n = i % 3
        print(f"Proceeding to the main game{loading[n]}  ", end="\r")
        time.sleep(0.25)
    progress_bar = [
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
        "[]",
    ]
    for i in range(len(progress_bar)):
        progress_bar[i] = "֍ "
        print("Internalizing" + " " + "".join(progress_bar), end="\r")
        time.sleep(0.5)
    print("\r")


def roll_animation():
    roll_list = [
        f"{Style.RESET_ALL}Common (1 in 2)                            ",
        f"{Fore.GREEN}{Style.NORMAL}Uncommon (1 in 4)                     ",
        f"{Fore.BLUE}{Style.NORMAL}Rare (1 in 8)                         ",
        f"{Fore.MAGENTA}{Style.NORMAL}Epic! (1 in 32)                 ",
        f"{Fore.YELLOW}{Style.NORMAL}Lengendary! (1 in 64)             ",
        f"{Fore.RED}{Style.NORMAL}Mythic!! (1 in 100)                          ",
        f"{Fore.WHITE}{Style.DIM}Secret!! (1 in 2000)                      ",
        f"{Fore.BLACK}{Style.BRIGHT}UNBELIVABLE!!! (1 in 10000)                        ",
        f"{Fore.GREEN}{Style.BRIGHT}INCOMPREHENSIBLE!!!! (1 in 40000)       ",
        f"{Fore.YELLOW}{Style.BRIGHT}JACKPOT!!!!!!! (1 in 1000000)                 "
    ]
