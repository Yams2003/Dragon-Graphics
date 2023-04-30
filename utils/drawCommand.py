from Command_Pattern.command import Command
from utils import settings


class DrawCommand(Command):
    def __init__(self, drawCache, grid, drawingColor):
        self.__drawCache = drawCache
        self.__grid = grid
        self.__drawingColor = drawingColor

    def execute(self):
        for pos in self.__drawCache:
            self.__grid[pos[0]][pos[1]] = self.__drawingColor

    def unexecute(self):
        print(self.__drawCache)
        for pos in self.__drawCache:
            self.__grid[pos[0]][pos[1]] = settings.BG_COLOR

