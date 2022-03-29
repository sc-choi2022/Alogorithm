T = int(input())

# babygin여부를 확인하는 함수 check
def check(card):
    # run 여부 확인
    for j in range(10 - 3 + 1):
        if card[j:j + 3].count(0) == 0:
            return True
    # triplet 여부 확인
    if max(card) >= 3:
        return True
    return False

for case in range(1, T+1):
    lst = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    ans = 0

    # 순서대로 카드를 p1, p2에 분배
    for i in range(len(lst)):
        if i%2 == 0:
            p1[lst[i]] += 1
            if check(p1):
                ans = 1
                break
        else:
            p2[lst[i]] += 1
            if check(p2):
                ans = 2
                break
    # 테스트 케이스 번호와 정답 출력
    print(f'#{case} {ans}')