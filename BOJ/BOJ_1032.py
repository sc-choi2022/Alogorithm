# 파일 이름의 개수 N
N = int(input())
# 첫번째 파일의 각 자리값을 리스트 check에 저장
check = list(input())

for _ in range(N-1):
    # N-1개의 파일명을 받아
    file = input()
    # 각자리를 비교하고 다르다면 check[i]에 '?' 저장
    for i in range(len(check)):
        if check[i] != file[i]:
            check[i] = '?'
# 패턴 출력
for c in check:
    print(c, end='')