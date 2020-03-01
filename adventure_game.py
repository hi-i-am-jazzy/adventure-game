import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself on a deserted dark hill in an old town in "
                "Transylvania.")
    print_pause("Where you have decided to venture to after some much needed "
                "inspiration for your next horror novel.")
    print_pause("You reach two brick road passageways.")
    print_pause("As you stare at both you notice one is dark, foggy, and "
                "mysteriously creepy.")
    print_pause("The other is leading to what looks like a town with an old "
                "vintage antique store called Magic Second Chance Antiques.")


def foggy_path(items):
    villians = ["Vampire", "Warlock", "Sorceror"]

    print_pause("You follow the dark foggy pathway and find an old Gothic "
                "Castle.")
    print_pause("You get up to the gigantic double doors of the castle and "
                "attempt to knock.")
    print_pause("As you're knocking one of the doors creeks open slowly and "
                "you hear a huge wisk of wind flow out...something is "
                "behind you!")
    print_pause(f"When you turn around a {random.choice(villians)} is "
                "behind you!!")
    villian_encounter_choice(items)


def store_path(items):
    if "Magical Axe of Perun" in items:
        print_pause("You go back into the store and the owner notices you "
                    "have taken the Axe and chases you out!")
        print_pause("You run out quickly back to the brick road!")
    else:
        print_pause("You follow the pathway to the vintage store.\nYou notice "
                    "the door slightly open so you peer inside and see many "
                    "interesting magical weapons.")
        print_pause("One catches your eye, it is the Magical Axe of Perun!\n"
                    "You take the Axe and walk back out into the brick road.")
        items.append("Magical Axe of Perun")
    brickroad_choice(items)


def fight_villian(items):
    if "Magical Axe of Perun" in items:
        print_pause("As it comes toward you, you take out the Magical Axe of "
                    "Perun and strike turning him to ash.")
        print_pause("That was a close call.")
        print_pause("You now have some material for your next book. Time to "
                    "fly home and start writing.")
    else:
        print_pause("You try to fend him off, but you fail and suffer a great "
                    "defeat.")
    play_again(items)


def villian_encounter_choice(items):
    print_pause("You can either try to fight or run away.")
    print_pause("Enter 1 to fight\nEnter 2 to run away.")
    fight_or_flight = input("(Please enter 1 or 2) ")
    if fight_or_flight == "1":
        fight_villian(items)

    elif fight_or_flight == "2":
        print_pause("You run back to the brick road.")
        brickroad_choice(items)

    else:
        print_pause("I did not understand, can you choose again?")
        villian_encounter_choice(items)


def brickroad_choice(items):
    print_pause("What path would you like to take?\nEnter 1 to go to the "
                "Foggy passage.\nEnter 2 to go to the Vintage Store.")
    passageway_choice = input("(Please enter 1 or 2) ")
    if passageway_choice == "1":
        foggy_path(items)
    elif passageway_choice == "2":
        store_path(items)
    else:
        print_pause("I did not understand, can you choose again?")
        brickroad_choice(items)


def play_again(items):
    play = input("Would you like to play again? (y/n) ")
    if "y" in play:
        items = []
        print_pause("Restarting game...")
        play_game()
    else:
        exit


def play_game():
    items = []
    intro()
    brickroad_choice(items)


play_game()
