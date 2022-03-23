import sys
sys.stdin = open('input.txt')

# 암호의 가장 마지막 숫자의 위치를 찾는 함수
def start(maze):
    for i in range(N):
        for j in range(M-1, 0, -1):
            if word[i][j] == 1:
                return i, j
# 암호해석 정보를 담은 딕셔너리 password
password = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}
T = int(input())
for case in range(1, T+1):
    # 배열의 세로크기 N, 가로크기 M
    N, M = map(int, input().split())
    # 암호코드 정보를 추출하여 담은 리스트 word
    word = [list(map(int, input()))for _ in range(N)]
    # 정답값 초기화
    ans = 0
    # 암호의 위치를 start함수를 통해 찾아 si, sj에 할당
    si, sj = start(word)

    # 암호 56개의 숫자를 담은 리스트를 secret변수에 할당
    secret = word[si][sj-55:sj+1]
    # secret 리스트의 값을 string값으로 변경하여 s_word에 할당
    s_word = ''
    for w in secret:
        s_word += ''+str(w)

    # 7개씩 s_word를 나눠 password딕셔너리를 이용하여 암호후보로 check 리스트에 추가
    check = []
    for c in range(0, len(s_word), 7):
        check.append(password[s_word[c:c+7]])

    # 암호리스트의 값으로 적당한 값인지 확인하기 위한 연산값 right
    right = (check[0] + check[2] + check[4] + check[6]) * 3 + check[1] + check[3] + check[5] + check[7]
    # 암호의 조건에 부합하면 ans에 sum(check)값을 할당
    if right%10 == 0:
        ans = sum(check)
    # 테스트케이스 번호와 ans 출력
    print(f'#{case} {ans}')