import time, character
def intro():
    yes = True
    while True:
        print("Intro")
        time.sleep(1)
        print("Myserious voice: 'I don't care! I seriously DON'T CARE! I have locked you up in my dungeon and you will never ever have the slightest of slimmer of hope in having the ability to even attempt to escape from this hell Ho of mine!")
        time.sleep(5)
        print("You wake up, dazed, who are you again?")
        player = character.Player(str(input("What is your name?")), 5)
        while yes:
            confirm = input(f"Are you sure your name is {player}?(y/n):")
            if confirm == "y":
                yes = False
            elif confirm == "n":
                  player = classes.Player(str(input("What is your name?")))
                

