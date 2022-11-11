from board import Board
from animals import VALUES_CALL
import random


# Function start app safari
def start_safari():

    board = Board()

    # Create board with animals
    board_at_start = board.animal_board_generator()

    # Output board at start
    board.board_output(board=board_at_start)

    # Create random values by row and by column
    row = random.randint(0, board.number_of_rows - 1)
    column = random.randint(0, board.number_of_columns - 1)

    # Find cell value
    cell_value = board_at_start[row][column]

    # Output chosen cell
    print(board.output_chosen_cell(row=row, column=column, cell_value=cell_value))

    # Create animal by the value in the cell
    animal = VALUES_CALL.get(cell_value)(board=board, board_at_start=board_at_start)

    # Determine which continuous cells the selected animal can conquer
    board_at_finish = animal.tries_to_conquer(row=row, column=column)

    # Added marker for convenience to find a cell
    board.mark_start_cell(row=row, column=column, board=board_at_finish)

    # Output board at finish
    board.board_output(board_at_finish)


if __name__ == '__main__':
    start_safari()
