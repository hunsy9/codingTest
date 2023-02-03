
sum=0
for i in list(range(1,1000000,2)):
    sum1=0
    for j in range(len(str(i))):
        sum1+=int(str(i)[j])
    sum+=sum1
print("The sum of the digits of odd numbers\nfrom 1 to one million is {:,}.".format(sum))
