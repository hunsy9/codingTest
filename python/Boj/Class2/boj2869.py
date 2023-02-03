#달팽이는 올라가고 싶다.

# A B V 를 입력 받는다. 그리고 달팽이의 높이를 h변수로 둔다.
h_snail=0
day_count = 0

A,B,V = map(int ,input().split())

while(h_snail==V):
    print("asdfasd")
    h_snail += A
    if (h_snail > V):
        day_count += 1
        break
    h_snail -= B
    day_count = day_count + 1

