import sys
sys.stdin = open('sample_input.txt')

# 전위 순회 함수 preorder, rootnode와 node값들을 담을 리스트 something
def preorder(root, something):
    cnt = something
    if root:
        # root값들을 cnt에 담는다.
        cnt.append(root)
        # 왼쪽 서브트리가 있으면 처리
        if len(arr[root]) >= 1:
           preorder(arr[root][0], cnt)
        # 오른쪽 서브트리가 있으면 처리
        if len(arr[root]) >= 2:
            preorder(arr[root][1], cnt)
    # root를 담을 리스트 cnt를 return
    return cnt

T = int(input())
for case in range(1, T+1):
    # 간선의 개수 E 시작 노드 N
    E, N = map(int, input().split())
    # E개의 부모 자식 노드 번호 쌍을 담을 리스트 info
    info = list(map(int, input().split()))
    # info의 정보를 정리하여 담을 리스트 arr
    arr = [[0]*2 for _ in range(E+2)]

    # info의 정보를 구분하여 arr에 추가
    for i in range(0, len(info), 2):
        if arr[info[i]][0] == 0:
            arr[info[i]][0] = info[i+1]
        else:
            arr[info[i]][1] = info[i+1]
    # 서브트리를 담은 리스트를 반환받을 리스트 cnt
    cnt = preorder(N, [])
    # 테스트케이스 번호와 서브트리개수 출력
    print(f'#{case} {len(cnt)}')