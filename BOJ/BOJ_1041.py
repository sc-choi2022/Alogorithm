import sys

# 주사위의 개수 N**3의 정수 N
N = int(sys.stdin.readline())
# 주사위의 숫자를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(sum(numbers)-max(numbers))
else:
    # 각 한 칸, 두 칸, 세 칸을 채우는 가장 작은 값 one, two, three
    one = min(numbers)
    two = min(min(numbers[0], numbers[5]) + min(numbers[1:5]),
              numbers[1]+numbers[2], numbers[1]+numbers[3], numbers[2]+numbers[4], numbers[3]+numbers[4])
    three = min(numbers[0]+numbers[1]+numbers[2], numbers[0]+numbers[1]+numbers[3], numbers[0]+numbers[2]+numbers[4], numbers[0]+numbers[3]+numbers[4],
                numbers[1]+numbers[2]+numbers[5], numbers[1]+numbers[3]+numbers[5], numbers[2]+numbers[4]+numbers[5], numbers[3]+numbers[4]+numbers[5])

    # 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값 answer
    answer = 0
    answer += one*((N-2)*(N-2) + 4*((N-1)*(N-2)))
    answer += two*(4*(N-2) + 4*(N-1))
    answer += three*4

    # answer 출력
    print(answer)