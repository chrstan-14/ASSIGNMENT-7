

def calculatePay(jobCode, hoursWorked):
    jobRates = {'L': 25, 'A': 30, 'J': 50}
    payRate = jobRates.get(jobCode.upper(), 0)

    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        grossPay = 40 * payRate + overtimeHours * payRate * 1.5
    else:
        grossPay = hoursWorked * payRate

    return payRate, grossPay

totalGrossPay = 0

while input("Do you want to enter employee data?: ") == "yes":
    lastName = input("Enter last name: ")
    jobCode = input("Enter job code: ")
    hoursWorked = float(input("Enter hours worked: "))

    payRate, grossPay = calculatePay(jobCode, hoursWorked)

    print("Last Name: " + lastName + ", Hours Worked: " + str(hoursWorked) + ", Pay Rate: $" + str(payRate) + ", Gross Pay: $" + str(grossPay))

    totalGrossPay = totalGrossPay + grossPay

print("Total Gross Pay for All Employees: $" + str(totalGrossPay))
