# 사람의 번호를 기준으로 함수 partition 진행
def partition(numbers):
    # 값이 하나 남을 때 그 리스트를 return
    if len(numbers) == 1:
        return numbers
    # middle을 기준으로 left, right를 구분
    middle = (len(numbers) + 1)//2
    left = partition(numbers[:middle])
    right = partition(numbers[middle:])

    # left와 right의 0번 인덱스 값이 대결하게 될 사람의 번호
    return rcp(left[0], right[0])

# 사람의 번호를 인덱스로 cards의 값을 확인
def rcp(numb_l, numb_r):
    # 같은 것을 낸다면 사람의 번호가 작은 사람이 승리한다.
    if cards[numb_l] == cards[numb_r]:
        return [min(numb_l, numb_r)]
    # card의 값의 차가 1이면 크기가 큰 쪽이 승리한다.
    elif abs(cards[numb_l] - cards[numb_r]) == 1:
        if cards[numb_l] > cards[numb_r]:
            return [numb_l]
        else:
            return [numb_r]
    # card의 값의 차가 2이면 크기가 작은 쪽이 승리한다.
    if abs(cards[numb_l] - cards[numb_r]) == 2:
        if cards[numb_l] < cards[numb_r]:
            return [numb_l]
        else:
            return [numb_r]

T = int(input())
for case in range(1, T+1):
    # 사람의 수 N
    N = int(input())
    # 가지고 있는 카드의 정보를 담은 리스트 cards
    cards = list(map(int, input().split()))
    # cards의 card의 index를 활용하기 위한 리스트 numbers
    numbers = [x for x in range(N)]

    # 테스트 케이스와 우승한 사람의 번호 + 1
    print(f'#{case} {partition(numbers)[0] + 1}')