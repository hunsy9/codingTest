infile = open('./text.txt','r')
mySet = set()
for line in infile:
    if line == '':
        mySet.add(line.rstrip())
