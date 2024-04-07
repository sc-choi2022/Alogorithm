from collections import defaultdict
import sys

color, number = defaultdict(int), defaultdict(int)
for _ in range(5):
    C, N = sys.stdin.readline().rstrip().split()
    color[C] += 1
    number[int(N)] += 1

color = sorted(list(color.items()), key=lambda x:(-x[1], x[0]))
number = sorted(list(number.items()), key=lambda x:(-x[1], x[0]))

# 카드의 점수를 출력
# 연속적인 숫자 확인
series = True
for i in range(1, len(number)):
    if number[i][0] != number[0][0] + i:
        series = False
        break

if color[0][1] == 5:
    # 1번
    if series:
        print(number[4][0] + 900)
    # 4번
    else:
        print(number[4][0] + 600)
# 2번
elif number[0][1] == 4:
    print(number[0][0] + 800)
elif number[0][1] == 3:
    # 3번
    if number[1][1] == 2:
        print(number[0][0] * 10 + number[1][0] + 700)
    # 6번
    else:
        print(number[0][0] + 400)
elif number[0][1] == 2:
    # 7번
    if number[1][1] == 2:
        print(number[1][0] * 10 + number[0][0] + 300)
    # 8번
    else:
        print(number[0][0] + 200)
# 5번
elif series:
    print(number[4][0] + 500)
# 9번
else:
    print(number[4][0] + 100)