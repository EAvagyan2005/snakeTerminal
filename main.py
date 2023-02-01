"""
we create a snake with 3 tail, a board, an apple, it moves to one of its 4 directions
when it eats the apple we create a tail and add it to the end, if it collides with border it dies

"""
from collections import deque
import keyboard
import time
from os import system
snake = deque([])
direction = 0 # 0 up, 1 right, 2 down, 3 left
dir_change = [(-1, 0), (0, 1), (1, 0), (0, -1)]
apple = (( ))
SIZES = (10, 20)
game_over = False

def start():
    head_x = SIZES[0]/2
    head_y = SIZES[1]/2
    snake.appendleft((head_x, head_y))
    snake.append((head_x-1, head_y))

def get_input():
    global direction
    if keyboard.is_pressed('w') and direction != 2:
        direction = 0
    elif keyboard.is_pressed('a') and direction != 1:
        direction = 3
    elif keyboard.is_pressed('s') and direction != 0:
        direction = 2
    elif keyboard.is_pressed('d') and direction != 3:
        direction = 1
def draw():
    print('#'*(SIZES[1]+2))
    for i in range(SIZES[0]):
        print('#', end='')
        for j in range(SIZES[1]):
            if (i, j) in snake:
                print("Z", end='')
            elif (i, j) == apple:
                print("a", end='')
            else:
                print(' ', end='')
        print('#')
    print('#'*(SIZES[1]+2))

def change():
    snake.pop()
    snake.appendleft((snake[0][0]+dir_change[direction][0], snake[0][1]+dir_change[direction][1]))
def check():
    if 0 <= snake[0][0] <= SIZES[0] and 0 <= snake[0][1] <= SIZES[1]:
        return
    global game_over
    game_over = True

if __name__ == "__main__":
    start()
    draw()
    print("Press S to start")
    keyboard.wait('s')
    iteration = 0
    while not game_over:
        get_input()
        check()
        if iteration % 6 == 0:
            change()
            system('cls')
            draw()
        time.sleep(0.05)
        iteration += 1

