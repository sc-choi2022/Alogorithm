# 문자열 S
S = input()
# 부분집합 ans
ans = set()

# 문자열 S의 첫번째 위치부터
for i in range(len(S)):
    # 부분 문자열을 나누어 ans에 추가 set으로 중복 제거
    for j in range(i, len(S)):
        ans.add(S[i:j+1])
# ans의 길이 출력
print(len(ans))