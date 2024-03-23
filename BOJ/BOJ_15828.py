from collections import deque
import sys

# 버퍼의 크기 N
N = int(sys.stdin.readline())
queue = deque([])
while True:
    # 라우터가 처리해야 할 정보 M
    M = int(sys.stdin.readline())
    # 입력의 끝
    if M == -1:
        break
    # 라우터가 패킷 하나를 처리한 경우
    elif M == 0:
        queue.popleft()
    else:
        # 버퍼가 꽉 차지 않은 경우
        if len(queue) < N:
            queue.append(M)
# 라우터에 남아있는 패킷을 앞에서부터 순서대로 공백으로 구분해서 출력
if queue:
    print(*queue)
# 비어있을 경우 empty 출력
else:
    print('empty')