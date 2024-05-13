import sys

# 일의 수 N
N = int(sys.stdin.readline())
# 처리하는 필요한 시간과 끝내야할 시간을 적은 명단 배열 todos
todos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 끝내야할 시간을 기준으로 정렬
todos.sort(key=lambda x:-x[1])
# 일을 하는 시간을 표시하는 배열 time
time = [0]*todos[0][1]
# 일을 모두 끝마칠 수 있는 지 여부를 저장하는 변수 flag
flag = True

for todo in todos:
    # 현재 일의 처리하는데 걸리는 시간 T와 끝내야할 시간 S
    T, S = todo
    # 현재 일을 처리한 시간 cnt
    cnt = 0
    for i in range(S-1, -1, -1):
        # 일을 time[i]시간에 처리할 수 있는 경우 time[i]에 표시 후 cnt 1 증가
        if not time[i]:
            time[i] = 1
            cnt += 1
        # 현재 일을 마친 경우 break
        if cnt == T:
            break
    # 현재 일을 마칠 수 없는 경우 flag를 False로 저장 후 break
    else:
        flag = False
        break

# 일을 모두 끝마칠 수 있는 경우
if flag:
    # 일을 모두 끝마칠 수 있는 가장 늦은 시간을 출력
    print(0 if all(time) else time.index(1))
# 일을 모두 끝마칠 수 없는 경우 -1 출력
else:
    print(-1)