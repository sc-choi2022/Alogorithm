import sys

while True:
    try:
        # 정수 N
        N = int(sys.stdin.readline())
    except:
        break
    answer = 1
    while True:
        if answer%N == 0:
            print(len(str(answer)))
            break
        answer *= 10
        answer += 1