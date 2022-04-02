from itertools import combinations
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # 식재료의 개수 N
    N = int(input())
    # 식재료의 시너지 값을 담은 리스트 ch
    ch = [list(map(int, input().split())) for _ in range(N)]

    # ch에 담긴 재료들의 이름이 0~N-1로 가정, 모든 재료이름 담은 리스트 ingr(index를 맞추기 위함)
    ingr = [x for x in range(N)]
    # 재료를 N//2로 나누기 위해 allof를 먼저 정의
    allof = list(combinations(ingr, N//2))

    # 가장 차이가 작은 값을 출력하기 위해 min_d값 초기화
    min_d = 10000
    # allof에 N//2개씩 나눈 값을 가지고
    for allo in allof:
        # ingr를 복사한 temp에서 allo의 값들을 제거하여 나머지 N//2의 재로를 담은 리스트 만든다.
        temp = ingr[::]
        for i in range(len(allo)):
            temp.remove(allo[i])
        allo_s = 0
        temp_s = 0
        # 시너지은 두개씩 확인하므로 allo와 temp에서 2개씩 선택하고
        mix1 = list(combinations(allo,2))
        mix2 = list(combinations(temp,2))
        # 시너지를 각각 allo_s와 temp_s에 담아준다.
        for m1 in mix1:
            allo_s += ch[m1[0]][m1[1]]
            allo_s += ch[m1[1]][m1[0]]
        for m2 in mix2:
            temp_s += ch[m2[0]][m2[1]]
            temp_s += ch[m2[1]][m2[0]]
        # 만약 abs(allo_s-temp_s)의 값이 min_d보다 작다면 min_d 재설정
        if abs(allo_s-temp_s) < min_d:
            min_d = abs(allo_s-temp_s)
    # 테스트케이스 번호와 min_d를 출력
    print(f'#{case} {min_d}')

def dfs(n, p1, p2):
    global ans

    # N개의 재료를 배분했다면
    if n == N:
        # 재료의 개수를 동일하게 분배했다면
        if len(p1) == len(p2):
            # 합을 초기화
            suma = sumb = 0
            # ingre의 시너지 값을 계산하는 이중 for문
            for i in range(len(p1)):
                for j in range(len(p1)):
                    suma += ingre[p1[i]][p1[j]]
                    sumb += ingre[p2[i]][p2[j]]
                # ans값과 비교하여 작은 값을 ans에 저장
            if ans > abs(suma - sumb):
                ans = abs(suma - sumb)
        return
    # n번째 재료를 p1혹은 p2에 배분
    dfs(n+1, p1 + [n], p2)
    dfs(n+1, p1, p2 + [n])

# 테스트 케이스 개수
T = int(input())
for case in range(1, T+1):
    # 식재료의 개수
    N = int(input())
    # 시너지값을 담은 리스트 ingre
    ingre = [list(map(int, input().split())) for _ in range(N)]
    # 최대 시너지 값로 ans 초기화
    ans = 20000*N//2
    dfs(0, [], [])
    # 테스트케이스 번호와 ans 출력
    print(f'#{case} {ans}')