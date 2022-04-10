import sys
sys.stdin = open('sample_input.txt')

T = int(input())

direct = (0,(-1,0),(1,0),(0,-1),(0,1))
opp = [0, 2, 1, 4, 3]
for case in range(1, T+1):
    # 행렬의 길의 N, 시간 M, 미생물 종류 수 K
    N, M, K = map(int, input().split())
    # 세로, 가로 위치, 미생물 수 , 이동 방향 순서로 K개의 정보를 담는다.
    lst = [list(map(int, input().split())) for _ in range(K)]

    # M시간이 경과한 결과를 반영
    for _ in range(M):
        # 존재하는 모든 미생물에 대해
        for j in range(len(lst)):
            # 위치를 방향에 맞춰 변경
            lst[j][0] = lst[j][0]+direct[lst[j][3]][0]
            lst[j][1] = lst[j][1]+direct[lst[j][3]][1]
            # 양품 위치에 도착하면
            if lst[j][0] in [0, N-1] or lst[j][1] in [0,N-1]:
                # 미생물의 수가 절반으로 줄고, 방향이 반대로 바뀐다.
                lst[j][2] //= 2
                lst[j][3] = opp[lst[j][3]]
        # lst의 값을 위치와 미생물 순서로 거꾸로 정렬한다.
        lst.sort(key=lambda x: (x[0],x[1],x[2]), reverse=True)

        n = 1
        # 모든 미생물 수를 확인할때까지
        while n < len(lst):
            # n-1와 n의 위치가 같으면
            if (lst[n-1][0], lst[n-1][1]) == (lst[n][0], lst[n][1]):
                # reverse를 했으므로 n-1값이 n보다 크다. 따라서 n-1의 미생물 개수를 증가시키고 n 미생물은 합병되어 사라진다.
                lst[n-1][2] += lst[n][2]
                lst.pop(n)
            else:
                # 동일하지 않다면 다음으로 넘어간다.
                n +=1
    # 남은 미생물 수를 구하여 담을 변수 ans
    ans = 0
    # lst의 미생물수를 ans에 더하여 준다.
    for ls in lst:
        ans += ls[2]
    # 테스트케이스 번호와 ans출력
    print(f'#{case} {ans}')