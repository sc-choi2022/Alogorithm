# 학생의 수 N
N = int(input())
# 학생 번호를 담을 리스트 numbers
numbers = [input() for _ in range(N)]

for i in range(1, len(numbers[0])+1):
    # 예비 학생 번호를 담을 리스트 info
    info = [-1] * N
    for j in range(N):
        # 예비 학생 번호가 이미 존재 하는 경우 break
        if numbers[j][-i:] in info:
            break
        # 예비 학생 번호를 info[j]에 저장
        info[j] = numbers[j][-i:]
    # 예비 학생 번호가 완성된 경우 i를 출력
    if -1 not in info:
        print(i)
        break