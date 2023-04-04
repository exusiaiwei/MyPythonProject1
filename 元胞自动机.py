import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 设置元胞自动机的规则
def update_rule(curr_board):
    rows, cols = curr_board.shape
    new_board = np.zeros((rows, cols))
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            count = np.sum(curr_board[i-1:i+2, j-1:j+2]) - curr_board[i][j]
            if curr_board[i][j] == 1:
                if count in [2, 3]:
                    new_board[i][j] = 1
            else:
                if count == 3:
                    new_board[i][j] = 1
    return new_board

# 初始化元胞自动机
def init_board(rows, cols, p):
    board = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if np.random.random() < p:
                board[i][j] = 1
    return board

# 创建动画
def animate(frame_num, img, board, update_func):
    new_board = update_func(board)
    img.set_data(new_board)
    board[:] = new_board[:]
    return img

# 设置元胞自动机的参数并运行动画
if __name__ == '__main__':
    rows = 100
    cols = 100
    p = 0.3
    board = init_board(rows, cols, p)
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='binary')
    ani = animation.FuncAnimation(fig, animate, fargs=(img, board, update_rule), interval=50)
    plt.show()
