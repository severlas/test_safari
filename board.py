import random


class Board:
    """Board generator and board output"""

    NUMBER_OF_ROWS: int = 10
    NUMBER_OF_COLUMN: int = 10
    LIST_ANIMALS: tuple = ('D', 'W', 'T', 'L')

    """initialization object class Board"""
    def __init__(
            self,
            number_of_rows: int = NUMBER_OF_ROWS,
            number_of_columns: int = NUMBER_OF_COLUMN,
            list_animals: tuple = LIST_ANIMALS
    ) -> None:
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.list_animals = list_animals

    """Animal board generator"""
    def animal_board_generator(self) -> list:
        board = [
            [random.choice(self.list_animals) for _ in range(self.number_of_columns)]
            for _ in range(self.number_of_rows)
        ]
        return board

    """Board output"""
    def board_output(self, board: list) -> None:
        line = ''.join(['+---' for _ in range(self.number_of_columns)]) + '+'
        separate = ' | '
        for el in range(self.number_of_rows):
            print(line)
            separate_columns = '| ' + separate.join(board[el]) + separate
            print(separate_columns)
        print(line)

    """Output message chosen cell"""
    @staticmethod
    def output_chosen_cell(row: int, column: int, cell_value: str) -> str:
        return f'Chosen cell: {row + 1}, {column + 1}: {cell_value}'

    """Mark start cell"""
    @staticmethod
    def mark_start_cell(row: int, column: int, board: list) -> None:
        board[row][column] = '^'
