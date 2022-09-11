import sys

# 주어지는 문자열 A, B
A, B = sys.stdin.readline().split()
# 출력할 ans값을 최대차이인 50으로 초기화
ans = 50

# A와 B의 길이차 많큼 확인이 필요
for i in range(len(B)-len(A)+1):
    # 매 확인마다 cnt을 통해 차이의 개수를 count
    cnt = 0
    for j in range(len(A)):
        # 만약 각 위치의 문자가 다르다면 cnt 1증가
        if A[j] != B[i+j]:
            cnt += 1
    # 현재 기준점에서의 cnt값과 ans중 작은 값을 ans에 저장
    ans = min(cnt, ans)
# 길이가 동일한 A,B의 차이를 최소가 될 때 그 차이를 출력
print(ans)