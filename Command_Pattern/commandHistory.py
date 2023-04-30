from queue import LifoQueue

class CommandHistory:
    def __init__(self):
        self.__undoCommands = LifoQueue(maxsize=0)
        self.__redoCommands = LifoQueue(maxsize=0)

    def pushCommandToUndo(self,command):
        self.__undoCommands.put(command)
        self.__redoCommands = LifoQueue(maxsize=0)

    def undo(self):
        if self.__undoCommands.empty():
            return
        command = self.__undoCommands.get()
        command.unexecute()
        self.__redoCommands.put(command)

    def redo(self):
        if self.__redoCommands.empty():
            return
        command = self.__redoCommands.get()
        command.execute()
        self.__undoCommands.put(command)

