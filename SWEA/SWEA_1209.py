import sys
sys.stdin = open("input.txt")

# 10번의 테스트 케이스에 대한 for문
for _ in range(1, 10+1):
    # 최댓값 초기화
    max_sum = 0
    # case에 케이스 번호 할당
    case = int(input())
    # lst에 100X100의 2차원 배열 할당
    lst = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합을 구하고 최댓값과 비교하여 최댓값 수정
    for i in lst:
        temp = sum(i)
        if temp > max_sum:
            max_sum = temp

    # 각 열의 합을 구하고 최댓값과 비교하여 최댓값 수정
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += lst[i][j]
        if temp > max_sum:
            max_sum = temp

    # 좌측에서 우측으로의 대각선에 대한 합을 구하고 최댓값과 비교하여 최댓값 수정
    for i in range(100):
        temp = 0
        temp += lst[i][i]
    if temp > max_sum:
        max_sum = temp

    # 우측에서 좌측으로의 대각선에 대한 합을 구하고 최댓값과 비교하여 최댓값 수정
    for i in range(100):
        temp = 0
        temp += lst[i][99-i]
    if temp > max_sum:
        max_sum = temp

    # 각 테스트 케이스의 번호와 최댓값을 출력
    print(f'#{case} {max_sum}')