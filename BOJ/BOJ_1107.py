import sys

def howmany():
    global answer
    for number in range(1000001):
        number = str(number)

        if abs(int(number)-N)+len(number) > answer:
            continue

        for i in range(len(number)):
            if int(number[i]) in broken:
                break
        else:
            answer = min(answer, abs(int(number)-N)+len(number))

# 이동하려고 하는 채널 N
N = int(sys.stdin.readline().rstrip())
# 고장난 버튼의 개수 M
M = int(sys.stdin.readline())
# 고장난 버튼를 저장하는 배열 broken
broken = list(map(int, sys.stdin.readline().split()))

answer = abs(100-N)
howmany()
print(answer)