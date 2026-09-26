import random

# Define snakes and ladders positions
# Key = start position, Value = end position
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    """Simulate rolling a 6-sided die."""
    return random.randint(1, 6)

def check_snake_or_ladder(position):
    """Check if the player landed on a snake or a ladder."""
    if position in snakes:
        print(f"Oops! Bit by a snake. Down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder. Up to {ladders[position]}")
        return ladders[position]
    return position

def play_game():
    player1_name = input("Enter Player 1 name: ").strip()
    player2_name = input("Enter Player 2 name: ").strip()
    
    p1_pos = 0
    p2_pos = 0
    
    turn = 0  # 0 for Player 1, 1 for Player 2
    
    while p1_pos < 100 and p2_pos < 100:
        if turn == 0:
            input(f"\n{player1_name}'s turn. Press Enter to roll dice...")
            dice_val = roll_dice()
            print(f"{player1_name} rolled a {dice_val}")
            
            if p1_pos + dice_val <= 100:
                p1_pos += dice_val
                p1_pos = check_snake_or_ladder(p1_pos)
                
            print(f"{player1_name}'s position: {p1_pos}")
            
            if p1_pos == 100:
                print(f"\nCongratulations! {player1_name} wins the game!")
                break
            turn = 1
            
        else:
            input(f"\n{player2_name}'s turn. Press Enter to roll dice...")
            dice_val = roll_dice()
            print(f"{player2_name} rolled a {dice_val}")
            
            if p2_pos + dice_val <= 100:
                p2_pos += dice_val
                p2_pos = check_snake_or_ladder(p2_pos)
                
            print(f"{player2_name}'s position: {p2_pos}")
            
            if p2_pos == 100:
                print(f"\nCongratulations! {player2_name} wins the game!")
                break
            turn = 0

if __name__ == "__main__":
    play_game()
