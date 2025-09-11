expense=[2200,2350,2600,2130,2190]

"""1"""
extra_in_feb=expense[1]-expense[0]
print(f"Expense in feb is {extra_in_feb}")

"""2."""
total_in_quarter=0
for i in range(3):
    total_in_quarter=expense[0]+expense[1]+expense[2]
print(f"Total in quarter is {total_in_quarter}")

"""3."""
if 2000 in expense:
    print("yes.")
else:
    print("no")
    

"""4."""
expense.append(1980)

"""5."""
expense[3]=expense[3]-200

print([i for i in expense])
