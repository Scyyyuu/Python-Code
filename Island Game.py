import random
import time

def print_slow(text):
    """Prints text with a slight delay for a more cinematic feel."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()

def play_game():
    # Game State
    hp = 100
    inventory = []
    monster_hp = 60
    has_escaped = False

    print_slow("--- Welcome to Castaway Island! ---")
    print_slow("Your boat crashed. You wake up on a sandy beach with nothing but your wits.")
    print_slow("Your goal: Find a way off this island alive.\n")

    while hp > 0 and not has_escaped:
        print(f"\n❤️ HP: {hp} | 🎒 Inventory: {inventory if inventory else 'Empty'}")
        print("Where would you like to go?")
        print("1. Explore the dark jungle 🌴")
        print("2. Search the shipwreck 🚢")
        print("3. Check the old stone cave 🪨")
        print("4. Attempt to build a raft 🔨")
        
        choice = input("> ").strip()

        if choice == "1":
            print_slow("\nYou march into the dense, dark jungle...")
            event = random.choice(["berry", "trap", "nothing"])
            
            if event == "berry":
                print_slow("✨ You find a bush filled with strange glowing berries! You eat them.")
                print_slow("+20 HP.")
                hp = min(100, hp + 20)
            elif event == "trap":
                print_slow("💥 Ouch! You step into an old hunter's snare trap.")
                print_slow("-15 HP.")
                hp -= 15
            else:
                print_slow("It's quiet. Too quiet. You find nothing but mosquitoes.")

        elif choice == "2":
            print_slow("\nYou swim out and climb into the tilting shipwreck...")
            if "Rusty Sword" in inventory:
                print_slow("You've already picked clean everything useful here.")
            else:
                print_slow("⚔️ Jackpot! Hidden inside a captain's chest, you find a Rusty Sword.")
                inventory.append("Rusty Sword")

        elif choice == "3":
            print_slow("\nYou venture into the pitch-black stone cave...")
            print_slow("👹 Sudden roar echoes! A mutated Island Goblin blocks your exit!")
            
            # Combat loop
            while monster_hp > 0 and hp > 0:
                print(f"\nGoblin HP: {monster_hp} | Your HP: {hp}")
                print("What do you do?")
                print("1. Attack")
                print("2. Run away")
                combat_choice = input("> ").strip()

                if combat_choice == "1":
                    if "Rusty Sword" in inventory:
                        damage = random.randint(15, 25)
                        print_slow(f"You swing your sword! You deal {damage} damage.")
                    else:
                        damage = random.randint(5, 12)
                        print_slow(f"You punch the goblin! You deal {damage} damage.")
                    
                    monster_hp -= damage
                    
                    if monster_hp > 0:
                        goblin_damage = random.randint(10, 18)
                        print_slow(f"The goblin slashes back! You take {goblin_damage} damage.")
                        hp -= goblin_damage
                elif combat_choice == "2":
                    print_slow("You successfully scramble out of the cave, terrified but alive!")
                    break
                else:
                    print("Invalid choice! The goblin bites you while you hesitate.")
                    hp -= 10

            if monster_hp <= 0:
                print_slow("\n🎉 You defeated the Goblin! Shiny metal parts spill out of its pockets.")
                print_slow("🔑 You picked up: Engine Gears.")
                inventory.append("Engine Gears")
                monster_hp = 9999 # Prevents fight from triggering again

        elif choice == "4":
            print_slow("\nYou gather logs on the beach to build a raft...")
            if "Engine Gears" in inventory:
                print_slow("🛠️ Using your Rusty Sword and the Engine Gears, you assemble a motorized raft!")
                print_slow("You push off into the sunset. You escaped the island!")
                has_escaped = True
            else:
                print_slow("You try to tie some logs together, but they float away. You need mechanical parts to build something sturdy.")
                print_slow("-5 HP from exhaustion.")
                hp -= 5
        else:
            print("Please type 1, 2, 3, or 4.")

    # Game Over Screens
    if has_escaped:
        print_slow("\n🏆 CONGRATULATIONS! YOU WON THE GAME! 🏆")
    elif hp <= 0:
        print_slow("\n💀 Game Over! You succumbed to the island's perils. Try again!")

if __name__ == "__main__":
    play_game()
