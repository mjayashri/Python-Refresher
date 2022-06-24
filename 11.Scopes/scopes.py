# Global scope
player_health = 10


def drink_portion():
    portion_strength = 2  # local scope
    print(portion_strength)
    print(player_health)


drink_portion()

# No  Block scope in python
game_level = 4
enemies = ["skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[2]

print(new_enemy)


# But
def create_enemy():
    if game_level < 5:
        new_enemy2 = enemies[0]


# print(new_enemy2)  # <= not available

# Modify the global variable (Not recommended)


def new_enemy():
    global new_one
    new_one = "Skeleton"


new_enemy()
print(new_one)

#  use return statements and call the function => recommended

# Global constants

PI = 3.14159  # Use it as capital letters
URL = "https://google.com"


def calc():
    print(PI * 4 * 4)


calc()
