# Fruit Ripness Checker

# fruits = {"banana", "Apple"}
# colors = {"Green": "Unripe ", "yellow": "ripe", "brown": "overripe"}

# fruit_color_combinations = {fruit: colors for fruit in fruits}

# print(fruit_color_combinations)

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print(f"The Colour is {color}, So {fruit} is Unripe.")
    elif color == "Yellow":
        print(f"The Colour is {color}, So {fruit} is Ripe.")
    elif color == "Brown":
        print(f"The Colour is {color}, So {fruit} is Ovverripe.")
