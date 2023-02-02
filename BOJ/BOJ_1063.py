import sys

# 킹의 위치 K, 돌의 위치 S, 움직이는 횟수 N
K, S, N = sys.stdin.readline().strip().split()
# 킹이 움직이는 종류를 담은 딕셔너리 move
move = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0], 'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
# 킹과 돌이 위치하는 체스판 배열 chess
chess = [[0] * 8 for _ in range(8)]
# 킹의 위치 ki, kj 돌의 위치 si, sj
ki, kj, si, sj = 8 - int(K[1]), ord(K[0]) - 65, 8 - int(S[1]), ord(S[0]) - 65
N = int(N)

for _ in range(N):
    # 킹이 움직여야하는 방향 word
    word = sys.stdin.readline().rstrip()

    # 행과 열의 방향을 변수 di, dj에 저장
    di, dj = move[word]
    # di, dj를 반형한 ki, kj의 다음 위치 ni, nj
    ni, nj = ki + di, kj + dj
    # ni, nj가 범위안에 있는 경우
    if 0 <= ni < 8 and 0 <= nj < 8:
        # ni, nj가 돌의 위치 si, sj인 경우
        if (ni, nj) == (si, sj):
            nii, njj = si + di, sj + dj
            # 돌이 킹에 의해 움직일 때 체스판을 벗어나지 않는 경우
            if 0 <= nii < 8 and 0 <= njj < 8:
                si, sj = nii, njj
            else:
                continue
        ki, kj = ni, nj
# 첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력
print(chr(65 + kj) + str(8 - ki))
print(chr(65 + sj) + str(8 - si))