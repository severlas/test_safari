from board import Board


class BaseAnimal:
    """Base animal"""

    # Base strength because we don't know which animal
    STRENGTH: int = 0

    """initialization object class BaseAnimal"""
    def __init__(self, board: Board, board_at_start: list) -> None:
        self.board = board
        self.board_at_start = board_at_start

    """Basic function to move the animal around the board"""
    def _move(self, row: int, column: int) -> bool:
        cell = self.board_at_start[row][column]
        if self.STRENGTH > CELL_VALUES.get(cell).STRENGTH and cell != '_':
            self.board_at_start[row][column] = '_'
            return True

    """Recursive function, animal tries to conquer cell"""
    def tries_to_conquer(self, row: int, column: int) -> list:
        if row < self.board.number_of_rows - 1:
            if self._move(row=row + 1, column=column):
                self.tries_to_conquer(row=row + 1, column=column)

        if row > 0:
            if self._move(row=row - 1, column=column):
                self.tries_to_conquer(row=row - 1, column=column)

        if column < self.board.number_of_columns - 1:
            if self._move(row=row, column=column + 1):
                self.tries_to_conquer(row=row, column=column + 1)

        if column > 0:
            if self._move(row=row, column=column - 1):
                self.tries_to_conquer(row=row, column=column - 1)

        if column < self.board.number_of_columns - 1 and row < self.board.number_of_rows - 1:
            if self._move(row=row + 1, column=column + 1):
                self.tries_to_conquer(row=row + 1, column=column + 1)

        if column > 0 and row > 0:
            if self._move(row=row - 1, column=column - 1):
                self.tries_to_conquer(row=row - 1, column=column - 1)

        if column < self.board.number_of_columns - 1 and row > 0:
            if self._move(row=row - 1, column=column + 1):
                self.tries_to_conquer(row=row - 1, column=column + 1)

        if column > 0 and row < self.board.number_of_rows - 1:
            if self._move(row=row + 1, column=column - 1):
                self.tries_to_conquer(row=row + 1, column=column - 1)

        return self.board_at_start


class Deer(BaseAnimal):
    """Deer"""

    # Deer doesn't defeat anyone
    STRENGTH: int = 1

    """Override method because Deer doesn't defeat anyone"""
    def tries_to_conquer(self, row: int, column: int) -> list:
        return self.board_at_start


class Wolf(BaseAnimal):
    """Wolf"""

    # Wolf defeats Deer
    STRENGTH: int = 2


class Tiger(BaseAnimal):
    """Tiger"""

    # Tiger defeats Wolves and Deer
    STRENGTH: int = 3


class Lion(BaseAnimal):
    """Lion"""

    # Lion defeats Tigers, Wolves and Deer
    STRENGTH: int = 4


CELL_VALUES = {
        '_': BaseAnimal,
        'D': Deer,
        'W': Wolf,
        'T': Tiger,
        'L': Lion
    }
