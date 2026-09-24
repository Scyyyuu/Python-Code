import random
import time

def cyberpunk_oracle():
    # ASCII Art Header
    print("=" * 60)
    print("      🌐 NEO-TOKYO DEEP-WEB ORACLE v0.92 [UNSTABLE] 🌐      ")
    print("=" * 60)
    
    # Fake terminal hacking simulation
    print("Connecting to the DarkNet Matrix...")
    time.sleep(1.0)
    print("Bypassing firewall proxies...")
    time.sleep(0.8)
    print("Decrypting central AI consciousness...")
    time.sleep(1.2)
    print("SYSTEM READY.\n")

    # Ask the user for their query
    question = input("⚡ What truth do you seek from the machine? > ")
    if not question.strip():
        print("❌ Error: The void cannot answer empty queries. Goodbye.")
        return

    print("\n[Crunching quantum probability matrices...]")
    time.sleep(1.5)

    # Database of chaotic cyberpunk answers
    responses = [
        "🟢 ACCESS GRANTED: The digital tides are in your favor. Proceed.",
        "🟢 ACCESS GRANTED: 100% probability of success. Buy more RAM.",
        "🟡 WARNING: Signal weak. The megacorporations are blocking this future.",
        "🟡 WARNING: Highly volatile. Unplug your router and try again tomorrow.",
        "🔴 ERROR 404: Future not found. Avoid all synthetic humans today.",
        "🔴 SECURITY BREACH: The AI has judged your question and it is laughing at you.",
        "⚫ SYSTEM CRASH: My sensors say 'No', but my malware says 'Go for it'.",
        "🔵 NOTICE: The prophecy is encrypted. Pay 5 Bitcoin to unlock response."
    ]

    # Print the randomized outcome
    print("\n" + "=" * 50)
    print(f"🔮 THE ORACLE RESPONDS:")
    print(random.choice(responses))
    print("=" * 50 + "\n")

if __name__ == "__main__":
    cyberpunk_oracle()
