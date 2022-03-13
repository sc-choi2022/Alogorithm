# 학생 수 N
N = int(input())
# 학생들이 뽑은 숫자를 담은 리스트 lst
lst = list(map(int, input().split()))
# 숫자에 맞게 정렬시킬 답 ans
ans = []
# N명의 뽑은 숫자에 대해
for i in range(N):
    # 0이면 제자리
    if lst[i] == 0:
        ans.insert(i, i+1)
    # 아니라면
    else:
        # 전체 길이에서 뽑은 수만큼 뺀 인텍스 위치에 수를 할당
        ans.insert(len(ans)-lst[i], i+1)
# 학생 번호 사이에는 한 칸의 공백을 가지고 출력
print(*ans)