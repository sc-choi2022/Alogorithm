import sys
sys.stdin = open('sample_input.txt')

def check(tri):
    # 이진법 수를 담은 리스트 bi의 위치 값들을 변경
    for i in range(len(bi)):
        # i위치의 값 변경
        bi[i] = (bi[i] + 1) % 2

        # 10진수 값을 저장할 변수 numb
        numb = 0
        # 10진수 값을 2진수로 numb에 저장한다.
        for idx in range(len(bi)):
            numb = numb*2 + bi[idx]

        # 기존 3진수와 비교하기 위해 리스트에 10진수 > 3진수 값 추가
        S = []
        temp = numb
        # 2진수 값을 3진수 값으로 변경하여 S에 저장
        while temp > 0:
            S.append(temp % 3)
            temp //= 3
        # 비교를 위해 tri와 동일한 방향으로 재정렬
        S = S[::-1]

        # 다른 위치의 개수 cnt 값 초기화
        cnt = 0
        # S와 tri중 작은 것을 기준으로
        for idx in range(min(len(S), len(tri))):
            # 위치의 값이 다르면 cnt 1증가
            if S[idx] != tri[idx]:
                cnt += 1
        # 길이가 다르다면 다른 값
        cnt += abs(len(S) - len(tri))
        # 한 위치만 다르다면 return numb
        if cnt == 1:
            return numb
        # 원래 상태로 복구
        bi[i] = (bi[i] + 1) % 2

T = int(input())
for case in range(1,T+1):
    # 이진수로 나타낸 수
    bi = list(map(int, input()))
    # 삼진수로 나타낸 수
    tri = list(map(int, input()))

    # check 함수로 나온 10진수 값
    ans = check(tri)
    # 테스트케이스 번호와 10진수 값 출력
    print(f'#{case} {ans}')