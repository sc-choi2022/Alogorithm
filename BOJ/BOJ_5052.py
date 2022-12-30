import sys

# 일관성여부를 확인하는 함수 check
def check(numbers):
    for i in range(N-1):
        for j in range(i + 1, N):
            # 일관성여부를 확인하는 numbers[i]의 길이 변수 length에 저장
            length = len(numbers[i])
            # 일관성이 없다면 NO을 return
            if numbers[i] == numbers[j][:length]:
                return 'NO'
    # 일관성이 있다면 YES를 return
    return 'YES'

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 전화번호 개수 N
    N = int(sys.stdin.readline())

    # 길이를 기준으로 전화번호를 담을 배열 numbers
    numbers = sorted([sys.stdin.readline().rstrip() for _ in range(N)], key=lambda x: len(x))
    # 함수 check에 매게변수로 배열 numbers을 담은 반환값을 변수 ans에 저장
    ans = check(numbers)
    # ans을 출력
    print(ans)