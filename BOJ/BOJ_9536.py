import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    howls = list(sys.stdin.readline().rstrip().split())
    while True:
        # 소리 sound
        sound = sys.stdin.readline().rstrip()
        # 질문이 주어지는 경우 울음소리를 출력
        if sound == 'what does the fox say?':
            print(*howls)
            break
        # 동물과 울음소리 정보가 주어지는 경우
        else:
            # 정보를 구분하여 저장 animals, goes, howl
            animals, goes, howl = sound.split()
            # 다른 동물의 울음소리 제외
            while howl in howls:
                howls.remove(howl)