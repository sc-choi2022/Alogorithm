import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    people = [0] * N

    for i in range(N):
        t1, t2 = map(int, sys.stdin.readline().split())
        people[i] = [t1, t2]

    peopleSort = sorted(people, key=lambda x : x[0])
    hired = 1
    man = peopleSort[0][1]

    for j in range(1, N):
        if peopleSort[j][1] < man:
            man = peopleSort[j][1]
            hired += 1
    print(hired)