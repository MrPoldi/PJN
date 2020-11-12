from datetime import datetime
import csv


class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return "Employee Name: " + self.name + "; Surname: " + self.surname + "; Salary: " + self.salary


class ReceivedInvoice:
    def __init__(self, date, amount):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount

    def __str__(self):
        return "Received Invoice Date: " + self.date.__str__() + "; Amount: " + self.amount


class IssuedInvoice:
    def __init__(self, date, amount):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount

    def __str__(self):
        return "Issued Invoice Date: " + self.date.__str__() + "; Amount: " + self.amount


employees = list()
recInvoices = list()
issInvoices = list()

with open("Employees.txt", "r", encoding="utf-8") as empFile:
    reader = csv.reader(empFile)
    for row in reader:
        employees.append(Employee(row[0], row[1], row[2]))

with open("ReceivedInvoices.txt", "r", encoding="utf-8") as recFile:
    reader = csv.reader(recFile)
    for row in reader:
        recInvoices.append(ReceivedInvoice(row[0], row[1]))

with open("IssuedInvoices.txt", "r", encoding="utf-8") as issFile:
    reader = csv.reader(issFile)
    for row in reader:
        issInvoices.append(IssuedInvoice(row[0], row[1]))

expenses = dict()
incomes = dict()
balance = dict()

salaries = 0
for emp in employees:
    salaries += int(emp.salary)

print(*employees, sep="\n")
print(*issInvoices, sep="\n")
print(*recInvoices, sep="\n")

print("Podaj zakres dat (YYYY-MM-DD): ")
print("Od: ")
dateFrom = datetime.strptime(input(), "%Y-%m-%d")
print("Do: ")
dateTo = datetime.strptime(input(), "%Y-%m-%d")

for year in range(dateFrom.year, dateTo.year+1):
    if year == dateFrom.year:
        for month in range(dateFrom.month, 13):
            expenses[f"{year}-{month}"] = salaries
            incomes[f"{year}-{month}"] = 0
            balance[f"{year}-{month}"] = 0
    elif year == dateTo.year:
        for month in range(1, dateTo.month+1):
            expenses[f"{year}-{month}"] = salaries
            incomes[f"{year}-{month}"] = 0
            balance[f"{year}-{month}"] = 0
    else:
        for month in range(1, 13):
            expenses[f"{year}-{month}"] = salaries
            incomes[f"{year}-{month}"] = 0
            balance[f"{year}-{month}"] = 0

for inv in recInvoices:
    if dateFrom <= inv.date <= dateTo:
        expenses[f"{inv.date.year}-{inv.date.month}"] += int(inv.amount)

print(expenses)

for inv in issInvoices:
    if dateFrom <= inv.date <= dateTo:
        incomes[f"{inv.date.year}-{inv.date.month}"] += int(inv.amount)

print(incomes)

for key in balance:
    balance[key] = incomes[key] - expenses[key]

print(balance)
