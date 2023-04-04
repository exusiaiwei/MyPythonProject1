import pygame
import random

# 游戏初始化
pygame.init()
width, height = 640, 480
speed = 20
direction = "right"

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# 蛇的初始位置和长度
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_len = len(snake_pos)

# 食物的初始位置
food_pos = [random.randrange(1, width // speed) * speed,
            random.randrange(1, height // speed) * speed]

# 游戏循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # 移动蛇
    if direction == "right":
        new_head = [snake_pos[0][0] + speed, snake_pos[0][1]]
    elif direction == "left":
        new_head = [snake_pos[0][0] - speed, snake_pos[0][1]]
    elif direction == "up":
        new_head = [snake_pos[0][0], snake_pos[0][1] - speed]
    elif direction == "down":
        new_head = [snake_pos[0][0], snake_pos[0][1] + speed]
    snake_pos.insert(0, new_head)
    snake_pos.pop()

    # 判断是否吃到食物
    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(1, width // speed) * speed,
                    random.randrange(1, height // speed) * speed]
        snake_len += 1

    # 绘制游戏场景
    screen.fill(black)
    pygame.draw.rect(screen, green, [food_pos[0], food_pos[1], speed, speed])
    for pos in snake_pos:
        pygame.draw.rect(screen, white, [pos[0], pos[1], speed, speed])
    pygame.display.update()

    # 判断是否结束游戏
    if snake_pos[0][0] < 0 or snake_pos[0][0] > width - speed \
            or snake_pos[0][1] < 0 or snake_pos[0][1] > height - speed:
        pygame.quit()
        quit()

    for pos in snake_pos[1:]:
        if pos == snake_pos[0]:
            pygame.quit()
            quit()

    pygame.time.Clock().tick(10)