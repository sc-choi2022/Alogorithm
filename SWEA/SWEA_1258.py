import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())
for case in range(1, T+1):
    # 양의 정수인 N
    N = int(input())
    # N x N 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 화학 물질이 담긴 용기들이 사각형의 행과 열의 길이 정보를 담을 딕셔너리 info
    info = {}
    # 화학 물질이 담긴 용기들이 사각형의 넓이를 담을 리스트 area
    area = []

    # arr에서 0이 아닌 곳을 찾아 열의 길이를 세고 info에 담는 for문
    for i in range(N):
        cnt = 0
        for j in range(N):
            # 값이 0이 아니라면 열의 길이 1 증가
            if arr[i][j] != 0:
                cnt += 1
            # 값이 0일 경우
            else:
                # 딕셔너리 info에 포함되지 않았다면 info에 추가 후 value 1로 할당
                if cnt in info:
                    info[cnt] += 1
                # 딕서너리에 이미 있는 key라면 value 1 증가
                else:
                    info[cnt] = 1
                # cnt 초기화
                cnt = 0

    # 사각형을 만들지 않는 0의 정보를 딕셔너리에서 삭제
    del(info[0])
    # 딕셔너리 info의 정보를 통해 사각형 넓이를 구하여 리스트 area에 값 추가
    for key in info:
        area.append(key*info[key])

    # 테스트 케이스 번호와 부분 행렬들을 개수 출력
    print(f'#{case} {len(area)}', end=' ')
    # 넓이가 동일한 경우 크기가 같을 경우 행이 작은 순으로 출력하고 중복하여 출력하지 않기 위해 set과 list를 활용
    area = list(set(area))
    # area를 정렬
    area.sort()
    # 딕셔너리의 값을 튜플로 reverse된 값으로 받아 sinfo에 할당
    sinfo = sorted(info.items(),reverse=True)

    # 행렬들의 행과 열의 크기를 출력
    for a in area:
        for key in sinfo:
            if a == key[1]*key[0]:
                print(f'{key[1]} {key[0]}', end=' ')
    print()