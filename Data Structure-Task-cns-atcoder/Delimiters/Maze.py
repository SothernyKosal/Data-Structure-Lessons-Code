from array import Array2D

class Maze:
    Maze_WALL ="*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "O"

    def __init__(self, numRow, numCols):
        self._mazeCells = Array2D(numRow,numCols)
        self._startCell = None
        self._exitCell = None

    def numRows(self):
        return self._mazeCells.numRows()
    def setStart