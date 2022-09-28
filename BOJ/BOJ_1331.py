# pi, pj에서 ci, cj로 나이트가 움직일 수 있는 지 확인하는 함수 right
def right(ci, cj, pi, pj):
    for di, dj in (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2):
        ni, nj = pi+di, pj+dj
        if ni == ci and nj == cj:
            # 가능하다면 True 반환
            return True
    # 불가능 하다면 False 반환
    return False

# 나이트 투어의 방문을 담을 행렬 tour
tour = [[0]*6 for _ in range(6)]
# 방문하는 칸과 tour의 위치값을 매칭할 딕셔너리 route
route = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
        '6': 0, '5': 1, '4': 2, '3': 3, '2': 4, '1': 5}
# 첫번째 위치를 리스트 first에 담는다.
first = list(input())
# 첫번째 위치 Fi, Fj
Fi, Fj = route[first[1]], route[first[0]]
# 이전 위치 pi, pj를 Fi, Fj로 초기화, ci, cj를 0, 0으로 초기화
pi, pj = Fi, Fj
ci, cj = 0, 0
for i in range(1, 36):
    # 위치값을 확인한 후 ci, cj에 할당
    info = list(input())
    ci, cj = route[info[1]], route[info[0]]
    # 이미 방문했거나 놓을 수 있는 위치가 아닌 경우 Invalid 출력 후 break
    if tour[route[info[1]]][route[info[0]]] or right(ci, cj, pi, pj) == False:
        print('Invalid')
        break
    # ci, cj 위치에 방문표시 후 pi, pj에 ci, cj할당
    tour[ci][cj] = 1
    pi, pj = ci, cj
else:
    # 모두 방문하고 돌아갈 수 없는 경우 Invalid 출력
    if right(Fi, Fj, ci, cj) == 0:
        print('Invalid')
    else:
        # Valid 출력
        print('Valid')