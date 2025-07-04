

def computeTuition(creditHours, districtCode):
    if districtCode == "I":
        ratePerHour = 250
    else:
        ratePerHour = 550

    tuitionOwed = creditHours * ratePerHour
    return tuitionOwed

totalTuitionOwed = 0

while input("Do you want to enter student data?") == "yes":
    lastName = input("Enter student last name: ")
    creditHours = int(input("Enter credit hours: "))
    districtCode = input("Enter district code: ")

    tuitionOwed = computeTuition(creditHours, districtCode)

    print("Student: " + lastName + ", Tuition Owed: $" + str(tuitionOwed))

    totalTuitionOwed = totalTuitionOwed + tuitionOwed

print("Total Tuition Owed by All Students: $" + str(totalTuitionOwed))
