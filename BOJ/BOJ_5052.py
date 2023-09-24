import sys

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 전화번호의 개수 N
    N = int(sys.stdin.readline())
    # 전화번호를 저장하는 목록 lst 정렬
    lst = [sys.stdin.readline().rstrip() for _ in range(N)]
    lst.sort()
    # 일관성 여부를 저장하는 변수 flag
    flag = True
    for i in range(N-1):
        L = len(lst[i])
        # 현재와 그 다음 번호를 비교
        if lst[i] == lst[i+1][:L]:
            flag = False
            break
    # 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력
    print('YES' if flag else 'NO')