# 로또 종이 출력을 위한 간단한 파이썬 코드

# 1부터 45까지의 번호를 갖는 로또 종이 출력
for i in range(1, 46):
    print("{:2d}".format(i), end=', ')

    # 매 7번째 번호마다 줄바꿈과 "repeat" 출력
    if i % 7 == 0:
        print("\n{}".format("repeat"))