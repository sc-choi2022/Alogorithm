import sys

# 로프의 개수
N = int(sys.stdin.readline())
# 로프의 정보를 담을 리스트 rope
rope = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
# 로프를 병렬로 연결했을 때의 중량을 담을 리스트 value
value = [rope[i]*(i + 1) for i in range(N)]
# 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량 출력
print(max(value))