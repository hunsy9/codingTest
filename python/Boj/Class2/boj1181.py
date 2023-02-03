N=int(input())
word_list=list(set([input() for i in range(N)]))
word_list.sort(key=lambda x: (len(x), x))
for i in range(len(word_list)):
    print(word_list[i])