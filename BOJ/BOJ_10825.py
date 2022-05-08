# 학생의 수 N
N = int(input())

info = ['']*N
# 이름, 국어, 영어, 수학
for i in range(N):
    # name, korean, english, math 값을 각각 받는다.
    name, korean, english, math = input().split()
    # 이름과 점수를 타입을 반영하여 info에 저장
    info[i] = [name, int(korean), int(english), int(math)]

# sorted()의 key값을 lambda를 활용하여 조건에 부합하게 정렬한 후 변수 answer에 저장한다.
answer = sorted(info, key= lambda x : (-x[1], x[2], -x[3], x[0]))
# answer의 각 값의 0번째 index 이름을 출력
for ans in answer:
    print(ans[0])