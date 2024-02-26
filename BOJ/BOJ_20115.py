import sys

# 에너지 드링크의 수 N
N = int(sys.stdin.readline())
# 에너지 드링크의 양을 저장하는 배열 drink
drink = sorted(list(map(int, sys.stdin.readline().split())))
# 페인이 최대로 만들 수 있는 에너지 드링크의 양 answer
answer = drink[-1] + sum(drink[:N-1])/2
# 최대로 만들 수 있는 에너지 드링크의 양을 출력
print(answer)