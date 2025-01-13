import sys

def howmany():
    global answer
    for number in range(1000001):
        number = str(number)

        # number를 눌러 움직일 수 있는 최소 횟수가 answer보다 많은 경우 continue
        if len(number)+abs(int(number)-N) > answer:
            continue

        for i in range(len(number)):
            # number에 고장난 버튼이 있는 경우
            if int(number[i]) in broken:
                break
        # answer값을 갱신
        else:
            answer = min(answer, abs(int(number)-N)+len(number))

# 이동하려고 하는 채널 N
N = int(sys.stdin.readline().rstrip())
# 고장난 버튼의 개수 M
M = int(sys.stdin.readline())
# 고장난 버튼를 저장하는 배열 broken
broken = list(map(int, sys.stdin.readline().split()))

# 채널 N으로 이동하기 위해 누르는 버튼의 최소값 answer
# 현재 100번에서 N번으로 이동하는 버튼 횟수로 초기화
answer = abs(100-N)
howmany()

# answer출력
print(answer)