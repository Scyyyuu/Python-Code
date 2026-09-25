import random
import time

def r_print(text):
    """Helper function to print text with a slight delay for dramatic effect."""
    print(text)
    time.sleep(0.6)

def rpg_battle():
    print("⚔️  Welcome to the Random RPG Arena! ⚔️\n")
    
    # Character stats: [HP, Max Damage, Accuracy %]
    player_hp = 100
    enemy_hp = 100
    enemy_name = random.choice(["Shadow Goblin", "Feral Orc", "Cyber Droid", "Skeletal Knight"])
    
    print(f"A wild {enemy_name} appears! Battle Start!\n")
    
    while player_hp > 0 and enemy_hp > 0:
        # --- PLAYER'S TURN ---
        r_print(f"❤️ Your HP: {player_hp} | 🖤 {enemy_name} HP: {enemy_hp}")
        input("Press Enter to swing your sword...")
        
        # Check if the attack hits
        if random.random() < 0.85:  # 85% accuracy
            # Calculate base damage
            damage = random.randint(10, 25)
            
            # Check for a critical hit (15% chance)
            if random.random() < 0.15:
                damage = int(damage * 1.5)
                r_print(f"💥 CRITICAL HIT! You slashed the {enemy_name} for {damage} damage!")
            else:
                r_print(f"⚔️ You struck the {enemy_name} for {damage} damage.")
                
            enemy_hp = max(0, enemy_hp - damage)
        else:
            r_print("💨 You swung and missed!")
            
        if enemy_hp <= 0:
            break
            
        print("-" * 40)
        
        # --- ENEMY'S TURN ---
        r_print(f"⚠️ {enemy_name} is winding up an attack...")
        
        # Player has a 10% chance to dodge
        if random.random() < 0.10:
            r_print("🤸 Quick reflexes! You completely dodged the attack!")
        else:
            enemy_damage = random.randint(8, 22)
            player_hp = max(0, player_hp - enemy_damage)
            r_print(f"💥 The {enemy_name} hits you back for {enemy_damage} damage.")
            
        print("=" * 40 + "\n")

    # --- BATTLE RESOLUTION ---
    if player_hp > 0:
        print(f"🏆 VICTORY! You defeated the {enemy_name}!")
    else:
        print(f"💀 GAME OVER! The {enemy_name} defeated you. Better luck next time!")

if __name__ == "__main__":
    rpg_battle()
