import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    AA, BB = sorted(list(A)), sorted(list(B))

    # 애너그램인지 아닌지를 예체 출력과 같은 형식으로 출력
    if AA == BB:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')