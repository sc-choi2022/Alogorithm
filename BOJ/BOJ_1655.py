from heapq import heappush, heappop
import sys

# 연산의 개수 N
N = int(sys.stdin.readline())
# 배열 중앙값을 기준으로 leftheap, rightheap을 나눈다.
leftheap = []
rightheap = []

for i in range(N):
    # 정수 x
    x = int(sys.stdin.readline())
    # leftheap과 rightheap의 길이가 같다면 leftheap
    # 최대힙형태로 x을 leftheap에 push
    if len(leftheap) == len(rightheap):
        heappush(leftheap, (-x, x))
    else:
        # 최소힙형태로 x을 rightheap에 push
        heappush(rightheap, (x, x))

    # leftheap에 rightheap의 값보다 큰 값이 있는지 확인
    if i > 0 and leftheap[0][1] > rightheap[0][1]:
        # leftheap의 가장 큰 값을 moveright, rightheap의 가장 작은 값을 moveleft에 저장
        moveright = heappop(leftheap)[1]
        moveleft = heappop(rightheap)[1]
        # leftheap에 최대힙형태로 moveleft push
        heappush(leftheap, (-moveleft, moveleft))
        # rightheap에 최소힙형태로 moveright push
        heappush(rightheap, (moveright, moveright))
    # 현재의 중앙값인 leftheap의 최대값을 출력
    print(leftheap[0][1])