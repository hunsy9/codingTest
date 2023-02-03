numbers=[int(input()) for i in range(9)]
print("{}\n{}".format(max(numbers),numbers.index(max(numbers))+1))