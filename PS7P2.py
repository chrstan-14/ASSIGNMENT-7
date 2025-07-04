

def batAvg(hits, atBats):
    return hits / atBats if atBats > 0 else 0

playerCount = 0

while input("Do you want to enter player stats?: ") == "yes":
    lastName = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    atBats = int(input("Enter number of at-bats: "))
    average = batAvg(hits, atBats)
    print(f"{lastName}'s Batting Average: {average:.3f}")
    playerCount += 1

print(f"Total players entered: {playerCount}")
