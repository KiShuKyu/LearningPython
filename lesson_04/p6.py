# Transportation mode selection

Vehicle = ("Car", "Walk", "Bike")
distance = 20

if 0 <= distance <= 3:
    print(f"You can walk {distance}km.")
elif 3 <= distance <= 15:
    print(f"You can use bike for {distance}km.")
elif 15 <= distance:
    print(f"You can use car for {distance}km.")
