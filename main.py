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

def flood_fill(grid, row, col, target_color, replacement_color):
    if grid[row][col] != target_color:
        return
    grid[row][col] = replacement_color
    if row > 0:
        flood_fill(grid, row - 1, col, target_color, replacement_color)
    if row < ROWS - 1:
        flood_fill(grid, row + 1, col, target_color, replacement_color)
    if col > 0:
        flood_fill(grid, row, col - 1, target_color, replacement_color)
    if col < COLS - 1:
        flood_fill(grid, row, col + 1, target_color, replacement_color)


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
drawCache = []


# list containing all the buttons available for use
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, drawing_color, "color", drawing_color),
    Button(90, button_y, 50, 50, WHITE, "eraser", BLACK),
    Button(170, button_y, 50, 50, WHITE, "clear", BLACK),
    Button(250, button_y, 50, 50, WHITE, "grid", BLACK),
    Button(330, button_y, 50, 50, WHITE, "fill", BLACK)
    ]

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            commandHistory.pushCommandToUndo(DrawCommand(drawCache, grid, drawing_color))
            drawCache = []
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                commandHistory.undo()
            if event.key == pygame.K_e:
                commandHistory.redo()
            if event.key == pygame.K_c:
                # Prompt the user for an RGB value
                r = int(input("Enter R value (0-255): "))
                g = int(input("Enter G value (0-255): "))
                b = int(input("Enter B value (0-255): "))
                drawing_color = (r, g, b)
                # Updating the color of the button based off color
                buttons[0].color = drawing_color
                buttons[0].text_color = drawing_color
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
                    if button.text == 'color':
                        # Prompt the user for an RGB value
                        r = int(input("Enter R value (0-255): "))
                        g = int(input("Enter G value (0-255): "))
                        b = int(input("Enter B value (0-255): "))
                        drawing_color = (r, g, b)
                    if button.text == "clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    if button.text == "eraser":
                        drawing_color = BG_COLOR
                    if button.text == "grid":
                        DRAW_GRID_LINES = not(DRAW_GRID_LINES)
                    # Updating the color of the button based off color
                    if button.text == "fill":
                        # Prompt the user to select a starting point for the fill
                        position = pygame.mouse.get_pos()
                        try:
                            row, col = get_row_col_from_pos(position)
                            target_color = grid[row][col]
                            replacement_color = drawing_color
                            flood_fill(grid, row, col, target_color, replacement_color)
                            drawCache = []
                            commandHistory.pushCommandToUndo(DrawCommand(drawCache, grid, drawing_color))
                        except IndexError:
                            pass
                    buttons[0].color = drawing_color
                    buttons[0].text_color = drawing_color
    draw(WIN, grid)

pygame.quit()
