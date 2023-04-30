import pygame

from Command_Pattern.commandHistory import CommandHistory
from utils import *
from utils.drawCommand import DrawCommand

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Graphics")
commandHistory = CommandHistory()

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)
    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    for button in buttons:
        button.draw(win)
    pygame.display.update()


def get_row_col_from_pos(position):
    x, y = position
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError
    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
drawCache = []


# list containing all the buttons available for use
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "ERASER", BLACK),
    Button(310, button_y, 50, 50, WHITE, "CLEAR", BLACK),
    Button(370, button_y, 50, 50, WHITE, "GRID", BLACK)
    ]

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(position)
                drawCache.append([row,col])
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(position):
                        continue
                    drawing_color = button.color
                    if button.text == "CLEAR":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    if button.text == "GRID":
                        DRAW_GRID_LINES = not(DRAW_GRID_LINES)
        if event.type == pygame.MOUSEBUTTONUP:
            commandHistory.pushCommandToUndo(DrawCommand(drawCache, grid, drawing_color))
            drawCache = []
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                commandHistory.undo()
            if event.key == pygame.K_e:
                commandHistory.redo()
    draw(WIN, grid)

pygame.quit()
