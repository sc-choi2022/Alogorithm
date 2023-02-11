import sys

# 테스트케이스의 번호 num
num = 1
# 연속하는 P일 중 L일만 사용가능한 캠핑장에 V일짜리 휴가
L, P, V = map(int, sys.stdin.readline().split())

while (P, L, V) != (0, 0, 0):
    # 최대 사용일 수 ans
    ans = V//P * L + (V%P if V%P < L else L)
    # 각 테스트케이스를 출력
    print(f'Case {num}: {ans}')

    L, P, V = map(int, sys.stdin.readline().split())
    # 테스트케이스 번호 1 증가
    num += 1