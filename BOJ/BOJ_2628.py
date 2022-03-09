# 종이의 가로와 세로의 길이 garo, sero
garo, sero = map(int, input().split())
# 칼로 잘라야하는 점선의 개수
N = int(input())

# 가로 선의 인덱스
g_idx = [garo]
# 세로 선의 인덱스
s_idx = [sero]

# 점선의 개수만큼 점선 정보를 g_idx와 s_dix에 담는다.
for _ in range(N):
    line, cut = map(int,input().split())
    if line == 1:
        g_idx.append(cut)
    else:
        s_idx.append(cut)
# g_idx와 s_idx를 정렬
g_idx.sort()
s_idx.sort()

# 가로의 가장 긴 길이를 찾는 for문
g_max = g_idx[0]
for i in range(1, len(g_idx)):
    if g_idx[i]- g_idx[i-1]> g_max:
        g_max = g_idx[i]- g_idx[i-1]

# 세로의 가장 긴 길이를 찾는 for문
s_max = s_idx[0]
for i in range(1, len(s_idx)):
    if s_idx[i]- s_idx[i-1] > s_max:
        s_max = s_idx[i] - s_idx[i-1]

# 가장 큰 종이 조각의 넓이를 출력
print(g_max * s_max)