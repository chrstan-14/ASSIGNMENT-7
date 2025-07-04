

def computeTotal(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.9  # Apply 10% discount
    return total

extendedPrice = 0

while input("Do you want to enter quantity and price?: ") == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    total = computeTotal(quantity, price)
    extendedPrice += total
    print(f"Quantity: {quantity}, Price: ${price:.2f}, Total after discount if applicable: ${total:.2f}")

print(f"Extended price (sum of all totals): ${extendedPrice:.2f}")
