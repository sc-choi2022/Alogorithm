# 선생님의 감시 범위를 확인하는 함수 check
def check():
    # check함수의 초기값을 YES로 초기화
    ans = 'YES'
    # 선생님의 모든 위치에서 확인을 한다.
    for teach in teacher:
        # 각 위치 si, sj
        si, sj = teach
        # 네 방향 기준이 될 di, dj를 설정
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            # k를 기준으로 while문을 활용해서 다음위치 ni,nj를 정한다.
            k = 1
            while k < 6:
                ni = si + di*k
                nj = sj + dj*k
                # 범위안의 위치인지를 확인
                if 0<= ni < N and 0 <= nj < N:
                    # 'O' 벽을 만나면 while문을 벗어난다.
                    if now[ni][nj] == 'O':
                        break
                    # 학생을 만나면 ans를 NO로 변경하고 ans를 반환한다.
                    elif now[ni][nj] == 'S':
                        ans = 'NO'
                        return ans
                k += 1
    return ans

# 벽을 세우는 함수 makeWall
def makeWall(cnt):
    global ans
    # 벽을 3개 세었다면
    if cnt == 3:
        # ans가 YES라면 이미 답을 찾았으므로 return
        if ans == 'YES':
            return
        # check의 반환값을 ans에 할당
        ans = check()
        return
    # now의 빈 곳 X를 벽 O로 만들고 복구하는 for문
    for i in range(N):
        for j in range(N):
            if now[i][j] == 'X':
                now[i][j] = 'O'
                makeWall(cnt+1)
                now[i][j] = 'X'
# NxN 크기의 길이 N
N = int(input())
# 현재 복도의 상태를 담은 리스트 now
now = [list(input().split()) for _ in range(N)]
# 선생님의 위치를 담을 리스트 teacher
teacher = []
# 출력할 ans값 초기화
ans = ''
# now에서 선생님'T'의 위치를 teacher에 저장
for i in range(N):
    for j in range(N):
        if now[i][j] == 'T':
            teacher.append((i, j))
# 벽이 없는 상태로 makeWall 함수를 실행
makeWall(0)
# 답을 출력
print(ans)