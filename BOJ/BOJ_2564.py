# 가로, 세로 길이
G, S = map(int, input().split())
# 상점의 수
N = int(input())
# 방향, 행, 열의 좌표를 담을 리스트 arr
arr = []

# N + 1개의 위치 관련 정보에 맞춰 arr에 추가
for _ in range(N + 1):
    d, length = map(int,input().split())
    if d == 1:
        arr.append([d, 0, length])
    elif d == 2:
        arr.append([d, S, length])
    elif d == 3:
        arr.append([d, length, 0])
    elif d == 4:
        arr.append([d, length, G])
# 동근이의 위치는 가장 마지막 정보
start = arr[-1]
# 최단 거리를 담을 리스트 add
add = []
# N개의 상점에 대한 for문
for i in range(N):
    # 동근이의 위치와 상점이 같은 거리에 있다면
    if start[0] == arr[i][0]:
        # 가로와 세로를 구분하여 최단 거리를 구한다.
        if start[0] == 1 or start[0] == 2:
            add.append(abs(start[2]-arr[i][2]))
        if start[0] == 3 or start[0] == 4:
            add.append(abs(start[1]-arr[i][1]))
    # 동근이의 위치와 상점이 다른 거리에 있다면
    else:
        # 평행한 위치의 거리에 있을 때
        if start[0] in [1, 2] and arr[i][0] in [1, 2]:
            temp1 = S + start[2] + arr[i][2]
            temp2 = S + (G - start[2]) + (G - arr[i][2])
            if temp1 >= temp2:
                add.append(temp2)
            else:
                add.append(temp1)
        elif start[0] in [3, 4] and arr[i][0] in [3, 4]:
            temp1 = S - start[1] + G + S - arr[i][1]
            temp2 = start[1] + G + arr[i][1]
            if temp1 >= temp2:
                add.append(temp2)
            else:
                add.append(temp1)
        # 평행하지 않은 위치들에 대한 최단거리
        elif start[0] == 1 and arr[i][0] == 3:
            add.append(start[2] + arr[i][1])
        elif start[0] == 1 and arr[i][0] == 4:
            add.append(G - start[2] + arr[i][1])
        elif start[0] == 2 and arr[i][0] == 3:
            add.append(start[2] + S - arr[i][1])
        elif start[0] == 2 and arr[i][0] == 4:
            add.append(G - start[2] + S - arr[i][1])
        elif start[0] == 3 and arr[i][0] == 1:
            add.append(start[1] + arr[i][2])
        elif start[0] == 3 and arr[i][0] == 2:
            add.append(S - start[1] + arr[i][2])
        elif start[0] == 4 and arr[i][0] == 1:
            add.append(start[1] + G - arr[i][2])
        elif start[0] == 4 and arr[i][0] == 2:
            add.append(S - start[1] + G - arr[i][2])
# 최단거리를 담은 리스트 arr의 모든 값을 더하고 출력
print(sum(add))