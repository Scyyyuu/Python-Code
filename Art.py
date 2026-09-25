import turtle
import random

def draw_random_art():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("🎨 Random Python Geometric Art Generator 🎨")
    
    # Set up the turtle artist
    artist = turtle.Turtle()
    artist.speed(0)  # Fastest drawing speed
    artist.width(2)
    
    # Hide the turtle icon so we only see the lines
    turtle.hideturtle()
    
    # Definie a bright, vibrant color palette
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF0", "#FFAF33"]
    
    # Generate a random number of steps for our design loop
    total_steps = random.randint(100, 250)
    
    # Pick a random angle deviation to make each run completely unique
    angle_offset = random.randint(45, 175)
    
    print(f"Creating a unique art piece with {total_steps} lines...")
    
    for step in range(total_steps):
        # Pick a random color from our palette
        artist.pencolor(random.choice(colors))
        
        # Move forward a distance that increases with each step
        artist.forward(step * 2)
        
        # Turn right by a dynamic angle
        artist.right(angle_offset)
        
        # Randomly jump to a new nearby spot occasionally to add asymmetry
        if step % 50 == 0 and step > 0:
            artist.penup()
            artist.goto(random.randint(-100, 100), random.randint(-100, 100))
            artist.pendown()

    print("✨ Art complete! Click on the graphics window to close it.")
    screen.exitonclick()

if __name__ == "__main__":
    draw_random_art()
