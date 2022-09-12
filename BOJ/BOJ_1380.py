import sys
# 시나리오 번호 cnt
cnt = 0

while True:
    # 여학생의 수 n
    n = int(sys.stdin.readline())
    # cnt 1 추가
    cnt += 1
    # n이 0이라면 break
    if n == 0:
        break
    # 이름을 담을 리스트 names
    names = [0] + [input() for _ in range(n)]
    # 리스트에 등장하는 횟수를 이름의 인덱스 위치에 담는 리스트 lst
    lst = [0]*(n+1)

    for _ in range(2*n-1):
        # 여학생 번호와 알파벳이 주어진다.
        idx, alpha = sys.stdin.readline().split()
        # lst[int(idx)] 값 1 증가
        lst[int(idx)] += 1

    for i in range(1, n+1):
        # lst에 값이 1인 경우
        if lst[i] == 1:
            # 시나리오 번호와 귀걸이를 돌려받지 못한 여학생의 이름을 출력
            print(cnt, names[i])