USPres = []

def president_sort(president):
    return sorted(president, key=lambda pres: len(pres.split()[-1]), reverse=True)

def print_president_order(name = "GERALD FORD"):
    global USPres
    print('The order of the {} president is {}'.format(name, USPres.index(name)))

def main():
    global USPres
    infile = open('USPres.txt', 'r')

    for line in infile:
        USPres.append(line.rstrip())

    USPres = [president.upper() for president in USPres]

    print('USPres data example:', USPres[:3])

    USPres = president_sort(USPres)

    print_president_order()
    print_president_order('JOHN KENNEDY')

main()

'''
[RUN]
USPres data example: ['GEORGE WASHINGTON', 'JOHN ADAMS', 'THOMAS JEFFERSON']
The order of the GERALD FORD president is 41
The order of the JOHN KENNEDY president is 19
'''
