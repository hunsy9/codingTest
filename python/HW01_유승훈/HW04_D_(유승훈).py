coefficient=float(input("Enter coefficient of restitution: "))
initial=float(input("Enter initial height in meters: "))
sum=initial
count=0
while initial>0.1:
    count+=1
    initial=initial*coefficient
    if initial<0.1:
        break;
    else:
        sum += (initial*2)
print("Number of bounces: {}".format(count))    
print("Meters traveled: {:.2f}".format((sum)))