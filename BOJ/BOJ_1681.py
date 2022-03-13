# 학생 수 N, 라벨에 미포함할 수 L
N, L = map(int, input().split())
L = str(L)
# N개의 값을 담을 리스트 arr
arr = []
# 양의 정수의 시작 수
num = 1
# 리스트 arr에 N개의 값이 담길 때까지
while len(arr) < N:
    # string 타입으로 변환한 num값이 L을 포함하지 않으면 arr에 추가
    s_num = str(num)
    if L not in s_num:
        arr.append(num)
    num += 1
# 라벨 중 가장 큰 수를 출력
print(arr[-1])