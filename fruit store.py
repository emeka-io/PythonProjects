# Simple Shopping Cart
# Goal: Simulate a real shopping system.
store = {"apple": 200, "banana": 150, 'orange': 200, 'watermelon': 300}
cart = { }
print("""
Welcome to the fruit store
Enter what you'd like to order, and the quantity.
Type "done" to stop ordering. Thank you.
""")

while True:
    item = input("Enter the item name (or 'done' to finish): ").lower()

    if item == 'done': # done to exit ordering
        break

    if item not in store:
        print('Sorry that item is not available')
        continue

    qaunt = int(input(f"How many {item}s do you want? "))

    # adding to cart
    if item in cart:
        cart[item] += qaunt
    else:
        cart[item] = qaunt


print('-----------------------------------')
print('RECEIPT')
print('-----------------------------------')
total = 0
for item, qty in cart.items():
    cost = store[item] * qty
    total += cost
    print(f"{item} x{qty} = ${cost}")


print('-----------------------------------')
print(f"Total = ${total}.00")
print('-----------------------------------')