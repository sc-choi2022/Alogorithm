# 모든 경우의 수의 연산을 진행하기 위한 dfs 함수
def dfs(idx):
    # 변수를 변경하기 위해 global을 활용
    global min_ans, max_ans, ans

    # 모든 수를 계산을 완료했다면
    if idx == N:
        min_ans = min(min_ans, ans)
        max_ans = max(max_ans, ans)
        return

    # 4개의 연산자에 대한 for문
    for i in range(4):
        # 이전 단계의 ans값을 변수 tmp에 할당
        tmp = ans
        # i번째 연산자의 사용할 수 있는 개수가 남았다면
        if operator[i] > 0:
            # 각 연산자에 맞는 계산을 하기 위한 if, elif, else문
            if i == 0:
                ans += numbers[idx]
            elif i == 1:
                ans -= numbers[idx]
            elif i == 2:
                ans *= numbers[idx]
            # 나누기 연산의 경우 고려사항이 존재한다.
            # 몫만을 취한다.
            else:
                # 음수와 양수에 따라 계산
                if ans >= 0:
                    ans //= numbers[idx]
                else:
                    ans = (-ans // numbers[idx]) * -1
            # 사용한 연산자의 가용 개수를 1줄이고 dfs(idx+1)를 실행한다.
            operator[i] -= 1
            dfs(idx + 1)
            # 변수 ans의 값에 tmp 할당
            ans = tmp
            # 연산자의 가용 개수를 돌려준다.
            operator[i] += 1


# 주어질 수의 개수
N = int(input())
# N개의 숫자를 담을 리스트 numbers
numbers = list(map(int, input().split()))
# 연산자 + - x / 각각의 개수 정보가 담긴
operator = list(map(int, input().split()))

# 출력할 최솟값 min_ans와 최댓값 max_ans의 초기값을 범위내 최댓값 최솟값으로 할당
min_ans = int(1e9)
max_ans = -int(1e9)

# ans는 계속해서 계산에 사용할 변수이다.
# number의 가장 첫번째 값을 ans에 할당
ans = numbers[0]

# 1번위치의 값부터 계산을 시작한다.
dfs(1)
# 모든 경우의 수로 계산 후 max_ans와 mix_ans 값을 출력한다.
print(max_ans)
print(min_ans)