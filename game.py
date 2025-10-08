import time
import random

# Global variables
inventory = []
health = 3

def pause():
    """Adds suspense."""
    time.sleep(1.5)

def intro():
    print("🌲 Welcome, traveler! You wake up lost in a mysterious forest...")
    pause()
    print("You see three paths ahead of you:")
    print("1. The River Path 🌉")
    print("2. The Cave Path 🔥")
    print("3. The Village Path 🌼")

def choose_path():
    """Ask player which path they choose."""
    choice = input("Which path do you take? (1, 2, or 3): ")
    if choice == "1":
        river_path()
    elif choice == "2":
        cave_path()
    elif choice == "3":
        village_path()
    else:
        print("That’s not a valid choice! Try again.\n")
        choose_path()

def find_item(item):
    """Add item to inventory."""
    inventory.append(item)
    print(f"You found a {item}! 🪙 Your inventory now: {inventory}")

def river_path():
    global health
    print("\n🌊 You walk toward the river and see a troll guarding the bridge.")
    pause()
    print("He growls, 'Pay the toll or face my wrath!'")
    action = input("Do you (1) fight the troll, (2) run away, or (3) offer a coin? ")
    
    if action == "1":
        print("You bravely fight the troll...")
        pause()
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print("💪 You defeat the troll and cross the bridge safely!")
            find_item("golden key")
        else:
            print("💀 The troll knocks you into the river! You lose 1 health.")
            health -= 1
    elif action == "2":
        print("You sprint away safely but feel cowardly. 😅")
    elif action == "3":
        if "coin" in inventory:
            print("You hand over the coin. The troll smiles and lets you cross.")
            find_item("bridge map")
        else:
            print("You have no coin! The troll laughs. You run away embarrassed.")
    else:
        print("Invalid choice — the troll gets impatient.")
        river_path()

def cave_path():
    global health
    print("\n🔥 You enter a dark cave. The air feels heavy...")
    pause()
    print("You hear something moving in the shadows.")
    action = input("Do you (1) light a torch, (2) sneak quietly, or (3) yell 'Who's there?': ")
    
    if action == "1":
        print("The light scares off a dragon sleeping nearby!")
        find_item("dragon scale")
    elif action == "2":
        print("You step on a bone and the dragon wakes up! 😱")
        health -= 1
        print("You lose 1 health and run out of the cave.")
    elif action == "3":
        print("A deep voice booms back: 'ME!' The dragon sneezes fire.")
        health -= 1
        print("🔥 You barely escape with your life!")
    else:
        print("You hesitate... the dragon notices you! Run!")
        cave_path()

def village_path():
    global health
    print("\n🏡 You find a peaceful village with friendly people.")
    pause()
    print("A kind woman greets you and offers two choices:")
    action = input("Do you (1) stay for dinner or (2) ask for directions home? ")
    
    if action == "1":
        print("You enjoy a delicious meal and gain energy! ❤️")
        health += 1
        find_item("coin")
    elif action == "2":
        print("They guide you safely out of the forest. You’re free! 🎉")
        print("🏆 Congratulations! You survived your adventure!")
    else:
        print("The villagers look confused. Try again.")
        village_path()

def check_health():
    global health
    print(f"\n❤️ Current Health: {health}")
    if health <= 0:
        print("💀 You faint from exhaustion. Game over!")
        return False
    return True

def play_game():
    global inventory, health
    inventory = []
    health = 3
    print("\n=== 🌟 MINI ADVENTURE GAME 🌟 ===\n")
    
    while True:
        intro()
        choose_path()
        if not check_health():
            break
        again = input("\nDo you want to explore another path? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing, traveler! Until next time.")
            break

# Run the game
play_game()
