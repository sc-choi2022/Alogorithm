# 목표하는 길이 X
X = int(input())
# 붙이는 막대의 개수
ans = 0
# 막대기 길이 L 64로 초기화
L = 64

# X를 만들기 위해 남은 길이가 있다면
while X:
    # L이 X보다 크다면
    if L > X:
        L //= 2
    else:
        # 현재 길이 L는 필요한 막대기로 목표 길이 X에서 L감소
        X -= L
        # 막대의 개수 1 증가
        ans += 1
# ans을 출력
print(ans)