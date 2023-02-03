annualRateOfInterest= int(input("annual rate of interest: "))
monthlyPayment= int(input("Enter monthly payment: "))
begBalance= int(input("Enter beg. of month balance: "))

def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):

    intForMonth = begBalance * (annualRateOfInterest/12) * 0.01 #월 초 잔고 * 한달 이율
    redOfPrincipal=monthlyPayment-intForMonth #월 납입 금액 - 달마다 내는 이자
    endBalance= begBalance-redOfPrincipal #과정을 거치고 남은 잔고

    return ( intForMonth , redOfPrincipal, endBalance)

x , y , z = calculateValues(annualRateOfInterest,monthlyPayment,begBalance) #함수에 매개변수 전달하고 리턴값받기
print("Interest paid for the month: ${:,.2f}".format(x))
print("Reduction of principal: ${:,.2f}".format(y))
print("End of month balance: ${:,.2f}".format(z))
