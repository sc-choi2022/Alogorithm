import sys
# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

def dfs(number):
    global cnt
    # 들어온 정수 number의 이어지는 다음 정수가 visited에 존재하지 않는다면
    if array[1][number] not in visited:
        # visited에 그 값을 추가하고 number를 그 값을 대체하여 dfs를 실행한다.
        visited.append(array[1][number])
        dfs(array[1][number])
    # 만약 그 값이 이미 visited에 존재(사이클이 끝)한다면 cnt 1 증가 후 return
    else:
        cnt += 1
        return

for _ in range(T):
    # 순열을 이루는 정수의 개수 N
    N = int(sys.stdin.readline())
    # 사이클을 이미 이룬 정수를 담을 리스트 visited
    visited = []
    # 순열을 배열로 표현한 방식으로 담을 array
    array = [0, 0]
    array[0] = [i for i in range(0, N + 1)]
    array[1] = [0] + list(map(int, sys.stdin.readline().split()))
    # 출력할 사이클의 수 cnt값 0으로 초기화
    cnt = 0

    # N까지 정수에 대해 visited에 존재하는 여부를 확인
    # 존재하지 않는다면 사이클확인이 필요하므로 dfs 실행
    for j in range(1, N + 1):
        if j not in visited:
            dfs(j)
    # 사이클의 수 cnt 출력
    print(cnt)