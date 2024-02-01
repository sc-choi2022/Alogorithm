import sys

# 사람들이 만나 기록의 수 N
N = int(sys.stdin.readline())
# 무지개 댄스르 추고 있는 이름을 저장하는 셋 rainbow
rainbow = {'ChongChong'}

for _ in range(N):
    # 만난 두 사람 A, B
    A, B = sys.stdin.readline().rstrip().split()

    if A in rainbow:
        rainbow.add(B)
    if B in rainbow:
        rainbow.add(A)

# 마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력
print(len(rainbow))