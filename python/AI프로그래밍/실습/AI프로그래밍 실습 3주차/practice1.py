infile = open('UN.txt', 'r')

nations = []

for line in infile:
    line = line.rstrip()
    nations.append(line.split(',')) #

print('Countries data example:', nations[:2])

asia_nations = []
for nation in nations:
    if nation[1] == 'Asia': #
        asia_nations.append(nation) #

print('The total number of Asian countries is', len(asia_nations))

for asia_nation in asia_nations:
    if not 'o' in asia_nation[0] or float(asia_nation[2]) < 30000 or float(asia_nation[1]) < 1.0: #
        idx = asia_nations.index(asia_nation) #
        del asia_nations[idx] #

print('Countries suitable for conditions: ')
for asian_nation in asia_nations[:-8:-2]:
    print(asian_nation[0])


    '''
[RUN]
Countries data example: [['Afghanistan', 'Asia', '31.8', '251772'], ['Albania', 'Europe', '3.0', '11100']]
The total number of Asian countries is 47
Countries suitable for conditions:
Vietnam
Turkey
Syrian Arab Republic
Republic of Korea
'''
