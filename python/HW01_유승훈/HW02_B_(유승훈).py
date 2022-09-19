beginningSalary=int(input("Enter beginning salary: "))
newSalary=beginningSalary*(1.05)*(1.05)*(1.05)*(1.05)
change=((newSalary-beginningSalary)/beginningSalary)*100
print("New salary: ${:,.2f}".format(newSalary))
print("Change: {:.2f}%".format(change))