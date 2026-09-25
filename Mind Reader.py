import time

def play_mind_reader():
    print("--- 🧠 WELCOME TO THE MIND READER AI 🎮 ---")
    print("Think of a secret number between 1 and 100.")
    print("Don't tell me! Keep it in your head.")
    print("I will try to guess it in 7 tries or less.\n")
    
    input("Press ENTER when you are ready to begin...")
    
    # Range bounds
    low = 1
    high = 100
    attempts = 0
    game_running = True

    while game_running:
        # Calculate the middle number mathematically
        guess = (low + high) // 2
        attempts += 1
        
        print(f"\n🤖 My guess #{attempts} is: {guess}")
        print("Is your number:")
        print("1. Higher than my guess")
        print("2. Lower than my guess")
        print("3. Exactly right! 🎉")
        
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == "1":
            low = guess + 1
        elif choice == "2":
            high = guess - 1
        elif choice == "3":
            print(f"\n🏆 Ta-da! I read your mind in just {attempts} tries!")
            game_running = False
        else:
            print("❌ Invalid choice. Please type 1, 2, or 3 based on your secret number.")
            attempts -= 1  # Don't penalize for a typo

        # Cheat detection check
        if low > high:
            print("\n🤨 Wait a minute... that's mathematically impossible!")
            print("Are you sure you didn't change your secret number or make a mistake?")
            game_running = False

if __name__ == "__main__":
    play_mind_reader()
