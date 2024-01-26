from collections import deque
import sys

def find(number):
    finding = deque(number)
    # 반환하는 시계수 numberR
    numberR = 10000

    for _ in range(4):
        tmp = finding[0]*1000+finding[1]*100+finding[2]*10+finding[3]
        numberR = min(numberR, tmp)
        finding.rotate(1)
    return numberR

# 입력되는 카드를 저장하는 배열의 시계수
card = deque(map(int, sys.stdin.readline().split()))
# 주어진 카드의 시계수
clock = find(card)
# 시계수를 개수를 저장하는 변수 answer
answer = 0

# 시작 시계수 start
start = 1111
while start <= clock:
    if find(list(map(int, list(str(start))))) == start:
        answer += 1
    start += 1

# 입력된 카드의 시계수가 모든 시계수들 중에서 몇 번째로 작은 시계수인지를 출력
print(answer)