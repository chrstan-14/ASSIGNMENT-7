

def tripStats(miles, gallons):
    mpg = miles / gallons if gallons > 0 else 0
    gasCost = gallons * 3.00
    return mpg, gasCost

tripCount = 0
totalMiles = 0
totalGas = 0

while input("Do you want to enter a trip?: ") == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))
    mpg, cost = tripStats(miles, gallons)
    print(f"Destination: {city}, Miles: {miles}, MPG: " + str(mpg), "Gas Cost: $" + str(cost))
    tripCount += 1
    totalMiles += miles
    totalGas += cost

print(f"Trips Entered: " + str(tripCount))
print(f"Total Miles: " + str(totalMiles))
print(f"Total Gas Cost: $" + str(totalGas))
