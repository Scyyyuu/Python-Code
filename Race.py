import random
import time
import os

def clear_screen():
    # Clears the terminal screen for a smooth animation effect
    os.system('cls' if os.name == 'nt' else 'clear')

def turtle_race():
    # Setup track length and racing turtles
    TRACK_LENGTH = 40
    turtles = {
        "🐢 Turbo-Tim": {"pos": 0, "icon": "🐢", "color": "Green"},
        "🚀 Shell-Shock": {"pos": 0, "icon": "🚀", "color": "Red"},
        "⚡ Nitro-Ned": {"pos": 0, "icon": "⚡", "color": "Yellow"}
    }
    
    input("🏁 Press ENTER to start the Mega Turtle Championship! 🏁")
    
    racing = True
    while racing:
        clear_screen()
        print("=" * (TRACK_LENGTH + 15))
        print("             THE GREAT TURTLE GRAND PRIX             ")
        print("=" * (TRACK_LENGTH + 15) + "\n")
        
        for name, data in turtles.items():
            # Calculate the spaces before and after the turtle to draw the track
            track_before = "-" * data["pos"]
            track_after = " " * (TRACK_LENGTH - data["pos"])
            print(f"{name:12} |{track_before}{data['icon']}{track_after}| FINISH")
            
            # Randomly advance each turtle by 0 to 3 spaces
            data["pos"] += random.randint(0, 3)
            
            # Check if anyone crossed the finish line
            if data["pos"] >= TRACK_LENGTH:
                data["pos"] = TRACK_LENGTH  # Cap at finish line
                racing = False
                
        print("\n" + "=" * (TRACK_LENGTH + 15))
        time.sleep(0.15) # Controls the speed of the animation

    # Determine the winner(s)
    winners = [name for name, data in turtles.items() if data["pos"] == TRACK_LENGTH]
    
    print("\n🏆 RACE OVER! 🏆")
    if len(winners) > 1:
        print(f"It's a tie between: {' and '.join(winners)}!")
    else:
        print(f"🎉 {winners[0]} dominates the track and wins! 🎉\n")

if __name__ == "__main__":
    turtle_race()
