from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Graphics")


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
    pygame.display.update()


def get_row_col_from_pos(position):
    x, y = position
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError
    return row, col


def plotline(row1, row2, col1, col2):
    drow = abs(row1 - row2)
    dcol = abs(col1 - col2)

    col = col1
    e = 0
    for row in range(row1, row2, -1):
        grid[row][col] = drawing_color
        e += dcol
        if (2 * e) > drow:
            col += 1
            e -= drow


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            initial = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            final = pygame.mouse.get_pos()
            row1, col1 = get_row_col_from_pos(initial)
            row2, col2 = get_row_col_from_pos(final)

            '''
            if col2 < col1:
                col1, col2 = col2, col1
                row1, row2 = row2, row1
            '''

            if row2 > row1 and col2 > col1:
                # Call plotline function with the original row and column values
                plotline(row1, row2, col1, col2)
            else:
                # Swap the starting and ending points to make sure the line is drawn correctly
                plotline(row2, row1, col2, col1)

            plotline(row1, row2, col1, col2)

        '''
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(position)
                grid[row][col] = drawing_color
            except IndexError:
                pass
        '''
    draw(WIN, grid)

pygame.quit()
