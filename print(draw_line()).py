def draw_line():
    return "======="

def draw_wall(height):
    wall = ""
    for _ in range(height):
        wall += "|      |\n"
    return wall

# 함수 호출 및 출력
print(draw_line())
print(draw_wall(2))
print(draw_line())
