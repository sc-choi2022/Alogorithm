from collections import deque
import sys
sys.stdin = open('input.txt')

# 10번의 테스트 케이스
for _ in range(10):
    # 테스트 케이스 번호
    case = int(input())
    # 8개의 숫자데이터를 deque()에 담아 code 생성
    code = deque(map(int, input().split()))

    # 사이클의 감소양을 첫 값 1로 초기화
    n = 1
    while True:
        # n이 5보다 커져 사이클 주기가 끝났다면 다시 1로 초기화
        if n > 5:
            n = 1

        # 처음 위치의 값에서 n을 뺀 변수 tmp
        tmp = code.popleft() - n

        # tmp가 0보다 작다면 0을 code에 추가하고 while문 탈출
        if tmp <= 0:
            code.append(0)
            break
        # tmp가 0보다 크다면 code에 값을 추가하고 계속 진행
        else:
            code.append(tmp)
        # 감소 값 1 증가
        n += 1
    # 테스트케이스 번호와 완성된 암호 출력
    print(f'#{case}', *code)