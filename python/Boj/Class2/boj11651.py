import sys
N = int(sys.stdin.readline())
xylist = [list(map(int,sys.stdin.readline().split())) for i in range(N) ]
xylist.sort(key=lambda x :(x[1],x[0]))
for i in xylist:
    print("{} {}".format(i[0],i[1]))