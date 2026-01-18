# adventure_game.py
# Advanced Text-Based Adventure Game

import random
import time

# Player data
player = {
    "name": "",
    "health": 100,
    "inventory": []
}


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def start_game():
    slow_print("\n🌍 Welcome to the Legendary Treasure Adventure!")
    player["name"] = input("Enter your name: ")
    slow_print(f"\nHello {player['name']}! Your quest begins...\n")

    while True:
        player["health"] = 100
        player["inventory"] = []

        result = crossroads()

        if result == "win":
            slow_print("\n🏆 YOU FOUND THE TREASURE! YOU WIN!")
        else:
            slow_print("\n💀 You failed your quest.")

        choice = input("\nPlay again? (yes/no): ").lower()
        if choice != "yes":
            break


def crossroads():
    slow_print("\nYou arrive at a crossroads.")
    slow_print("1. Enter the forest")
    slow_print("2. Enter the cave")

    choice = input("Choose (1/2): ")

    if choice == "1":
        return forest()
    elif choice == "2":
        return cave()
    else:
        slow_print("Invalid choice.")
        return "lose"


def forest():
    slow_print("\n🌲 You enter the dark forest...")
    slow_print("You find a sword on the ground.")
    player["inventory"].append("sword")

    slow_print("1. Follow the river")
    slow_print("2. Climb a tree")

    choice = input("Choose (1/2): ")

    if choice == "1":
        return river_event()
    elif choice == "2":
        slow_print("\nYou spot treasure from above and go there safely.")
        return "win"
    else:
        return "lose"


def river_event():
    slow_print("\n🌊 A wild beast appears!")

    if "sword" in player["inventory"]:
        slow_print("You use your sword to fight!")
        if random.randint(1, 10) > 3:
            slow_print("You defeated the beast!")
            return "win"
        else:
            player["health"] -= 50
            slow_print("You got injured and lost.")
            return "lose"
    else:
        slow_print("You have no weapon. You lose.")
        return "lose"


def cave():
    slow_print("\n🕳️ You enter the cave...")

    slow_print("1. Light a torch")
    slow_print("2. Walk in darkness")

    choice = input("Choose (1/2): ")

    if choice == "1":
        return puzzle_room()
    elif choice == "2":
        slow_print("You fall into a pit.")
        return "lose"
    else:
        return "lose"


def puzzle_room():
    slow_print("\n🔐 Solve this puzzle to proceed:")
    answer = input("What is 8 * 7? ")

    if answer == "56":
        slow_print("Correct! You found the treasure!")
        return "win"
    else:
        slow_print("Wrong answer. Cave collapses.")
        return "lose"


if __name__ == "__main__":
    start_game()