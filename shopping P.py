menu = {"pizza":3.00,
        "nachos": 4.50,
        "popcorn": 2.50,
        "fries":1.00,
        "soda":3.00,
        "lemonade": 4.25
        }

cart = []
total = 0


print("---menu---")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("----------")

while True: 
    food = input("Select an item: (q to quit) ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------")
for food in cart:
    total += menu.get(food)
    print(food, end=", ")

print("\n----------")
print(f"Your total is: {total:.2f}")