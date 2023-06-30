import sys

# 라운드 수 R
R = int(sys.stdin.readline())
# 상근이가 낸 sanggeun
sanggeun = sys.stdin.readline().rstrip()
# 친구의 수 N
N = int(sys.stdin.readline())
friends = [sys.stdin.readline().rstrip() for _ in range(N)]

check = {'R':0, 'S':1, 'P':2}
score = maxScore = 0

for i in range(R):
    lst = [['R', 0], ['S', 0], ['P', 0]]
    for j in range(N):
        if (check[sanggeun[i]] + 1) % 3 == check[friends[j][i]]:
            score += 2
        elif sanggeun[i] == friends[j][i]:
            score += 1

        for l in lst:
            if (check[l[0]]+1)%3 == check[friends[j][i]]:
                l[1] += 2
            elif l[0] == friends[j][i]:
                l[1] += 1
    maxScore += max(lst)[1]
print(score)
print(maxScore)