import sys
# 목표 합의 값 N, 연속된 숫자의 개수 L
N, L = map(int, sys.stdin.readline().split())

# 최소 L개부터 100개까지 확인
for i in range(L, 101):
    # i로 나누어 나누어 떨어지는 것을 확인하기 위한 x
    x = N - ((i+1)*i)//2
    # x이 i개의 숫자로 나누어떨어지는 경우
    if x%i == 0:
        x = int(x//i)
        # 음수가 아닌 정수인 경우
        if x >= -1:
            # 조건에 맞게 출력
            for j in range(1, i + 1):
                print(x + j, end=' ')
            print()
            break
# 그런 수열이 없는 경우 -1 출력
else:
    print(-1)