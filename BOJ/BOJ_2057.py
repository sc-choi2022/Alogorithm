import sys

# 정수 N
N = int(sys.stdin.readline())
# 팩토리얼을 저장하는 배열 factorial
factorial = [1, 1] + [0]*18
for i in range(2, 20):
    factorial[i] = factorial[i-1]*i

# 팩토리얼을 더해 정수 N을 만드는 변수 answer
answer = 0

for j in range(19, -1, -1):
    if answer + factorial[j] < N:
        answer += factorial[j]
    # N을 서로 다른 정수 M개의 팩토리얼의 합으로 나타낼 수 있으면 YES 출력
    elif answer + factorial[j] == N:
        print('YES')
        break
# 없다면 NO 출력
else:
    print('NO')