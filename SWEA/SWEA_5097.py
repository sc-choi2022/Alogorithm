from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # 수열을 이루는 숫자의 개수 N, 이동 횟수 M
    N, M = map(int, input().split())
    # 수열을 담은 queue numbers
    numbers = deque(map(int, input().split()), maxlen=N)

    # M번만큼 이동시키는 for문
    for i in range(M):
        tmp = numbers.popleft()
        numbers.append(tmp)
    # 테스트 케이스번호와 numbers의 첫 숫자를 출력
    print(f'#{case} {numbers[0]}')