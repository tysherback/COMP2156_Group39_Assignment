import random

def roll_die():
    return random.randint(1, 6)

if __name__ == "__main__":
    result = roll_die()
    print(f"You rolled a {result}")