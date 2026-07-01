import csv
goal=25000
expenses=[]
try:
    with open("expenses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['amount']= int(row['amount'])
            except ValueError:
                print("skipping invalid amount:",row['amount'])
                continue
            expenses.append(row)
except FileNotFoundError:
    print("error: expenses.csv not found")
print(expenses)

category_totals = {}

for e in expenses:
    cat= e["category"]
    amt= e["amount"]
    if cat in category_totals:
        category_totals[cat] = category_totals[cat] + amt
    else:
        category_totals[cat] = amt
print(category_totals)
u=sum(category_totals.values())
print("grand value",u)
print("remaining to earn", goal-u)