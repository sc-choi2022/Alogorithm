import sys

def dfs():
    # 6개의 수가 골라졌다면 출력
    if len(lotto) == 6:
        print(*lotto)
        return

    for s in S:
        # 사전순으로 출력하고 중복 수가 없도록 if문을 활용
        if s > lotto[-1]:
            lotto.append(s)
            dfs()
            lotto.pop()

while True:
    # 주어지는 테스트케이스를 리스트 S에 저장
    S = list(map(int, sys.stdin.readline().split()))
    # 마지막 줄 0이 주어졌다면 break
    if S == [0]:
        break
    # 첫번째 수를 S에서 pop하여 변수 k에 저장
    k = S.pop(0)
    # 6개을 담는 첫번째 수로 가능한 idx의 값을 리스트 lotto에 담아 함수 dfs 실행
    for idx in range(k-6+1):
        lotto = [S[idx]]
        dfs()
    # 테스트 케이스 사이에 빈 줄을 출력
    print()