a= int(input())
price = 1000 - a
list=[500,100,50,10,5,1]
count = 0
for i in list:
    count = count + int(price/i)
    price = price - int(price/i)*i
print(count)

