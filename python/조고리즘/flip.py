def check_reverse_from_front(fishes):
    origin_v = 0
    origin_i = 0

    for i in range(len(fishes)):
        if fishes[i] != i + 1:
            origin_v = i + 1
            for j in range(i, len(fishes)):
                if abs(fishes[j]) == origin_v:
                    origin_i = j
                    break

            fishes[i:origin_i + 1] = fishes[i:origin_i + 1][::-1]
            for j in range(i, origin_i + 1):
                fishes[j] *= -1
            break

    for i in range(len(fishes)):
        if fishes[i] != i + 1:
            return False
    return True


def check_reverse_from_back(reversed_fish):
    org_value, org_idx = 0, 0

    for i in range(len(reversed_fish) - 1, -1, -1):
        if reversed_fish[i] != i + 1:
            org_value = i + 1
            for j in range(i, -1, -1):
                if abs(reversed_fish[j]) == org_value:
                    org_idx = j
                    break

            reversed_fish[org_idx:i + 1] = reversed_fish[org_idx:i + 1][::-1]
            for j in range(org_idx, i + 1):
                reversed_fish[j] *= -1
            break

    for i in range(len(fishes)):
        if fishes[i] != i + 1:
            return False
    return True


n = int(input())

for i in range(5):
    fishes = list(map(int, input().split()))
    reversed_fish = fishes[::-1]

    if check_reverse_from_front(fishes):
        print("one")
    else:
        check_reverse_from_back(reversed_fish)
        if check_reverse_from_front(fishes) or check_reverse_from_back(reversed_fish):
            print("two")
        else:
            print("over")




