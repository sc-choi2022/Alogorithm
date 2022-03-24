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