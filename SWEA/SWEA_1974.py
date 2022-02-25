import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수
T = int(input())
for case in range(1, T+1):
    # 9 x 9 크기의 퍼즐의 데이터를 리스트 arr에 할당
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 리스트 arr의 전치행렬(세로 탐색을 slicing으로 하기 위함)
    trans = list(map(list,zip(*arr)))
    # temp리스트 생성할 때 스도쿠 조건을 만족한다면 정렬시 check 리스트와 동일
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 0 혹은 1의 값이 나와야하므로 확인을 위해 ans를 -1로 초기화
    ans = -1

    # 총 9개의 행에 대해 모든 9개의 값
    # 슬라이싱을 통해 arr와 trans를 확인하는 temp리스트를 생성
    # temp1, 2를 정렬
    for k in range(9):
        temp1 = arr[k][:]
        temp1.sort()
        temp2 = trans[k][:]
        temp2.sort()
        # 1~9를 정렬하여 가진 check와 비교하여 다르다면 스도쿠가 성립하지 않으므로 ans에 0 할당
        if temp1 != check:
            ans = 0
        elif temp2 != check:
            ans = 0
    # 3 x 3 크기의 작은 격자에 대해 temp3를 생성
    if ans != 0:
        for i in range(0, 6+1, 3):
            for j in range(0, 6+1, 3):
                temp3 = []
                for ii in range(3):
                    for jj in range(3):
                        temp3.append(arr[i+ii][j+jj])
                # temp3 정렬
                temp3.sort()
                # check와 비교하여 다르다면 스도쿠가 성립하지 않으므로 ans에 0 할당
                if temp3 != check:
                    ans = 0
    # 위 단계를 통해 ans가 0이 되지 않고 -1이라면
    if ans == -1:
        # 스도쿠 성립하므로 ans에 1할당
        ans = 1
    # 테스트 케이스 번호와 정답 출력
    print(f'#{case} {ans}')