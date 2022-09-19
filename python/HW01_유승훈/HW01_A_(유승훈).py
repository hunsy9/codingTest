pPrice=int(input("Enter purchase price: "))
sPrice=int(input("Enter selling price: "))
markup=sPrice-pPrice
percentageMarkup=(markup/pPrice)*100
profitMargin=(markup/sPrice)*100
print("Markup: ${:.1f}".format(markup))
print("Percentage markup: {}%".format(percentageMarkup))
print("Profit margin: {:.2f}%".format(profitMargin))