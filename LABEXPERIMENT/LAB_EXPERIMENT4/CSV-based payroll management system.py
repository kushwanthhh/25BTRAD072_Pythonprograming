import csv

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        print("Employee Payroll Summary")

        for row in reader:
            name = row["Name"]
            basic = float(row["Basic"])
            allowance = float(row["Allowance"])

            gross = basic + allowance
            deduction = basic * 0.10
            net = gross - deduction

            print("\nName:", name)
            print("Gross Salary:", gross)
            print("Deduction:", deduction)
            print("Net Salary:", net)

except FileNotFoundError:
    print("CSV file not found")
