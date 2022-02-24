import sys
sys.stdin = open('input.txt')
# 테스트 케이스의 수 T
T = int(input())

for case in range(1, T + 1):
    # 카드 수 N
    N = int(input())
    # 카드가 놓인 순서대로 N개의 카드 이름 리스트 arr에 할당
    arr = list(input().split())
    # 카드 수를 구분할 절반 half을 홀수와 짝수에 따라 결정
    if N % 2:
        half = N // 2 + 1
    else:
        half = N // 2
    # 케이스 번호 출력
    print(f'#{case}', end=' ')

    while True:
        # half의 앞쪽은 0번 인덱스를 출력 후 pop
        print(arr[0], end=' ')
        arr.pop(0)
        # pop 이후 arr가 비어있다면 while문 탈출
        if arr == []:
            break

        # half의 뒤쪽은 half-1를 인덱스로 출력 후 pop
        print(arr[half - 1], end=' ')
        arr.pop(half - 1)
        # pop 이후 arr가 비어있다면 while문 탈출
        if arr == []:
            break
        else:
            # 비어 있지 않다면 half 1 감소
            half -= 1
    # 테스트 케이스 마다 구분하기 위한 print문
    print()