from .data_format import *
from src.game.keyboard import KeyBuffer
from src.game.tetris import Tetris

import threading


class MyTetris(Tetris):
    def __init__(self, ratio=20):
        super().__init__(ratio)

    def set_key_buffer(self, key_buffer: KeyBuffer):
        self.key_buffer = key_buffer
    
    def set_condition(self, condition: threading.Condition):
        self.condition = condition

    def set_display_method(self, next, held, board):
        self.display_next = next
        self.display_held = held
        self.display_board = board

    def display(self):
        next = TetrisSmallBlock("Next", self.next_piece.coords, self.next_piece.color)
        held = TetrisSmallBlock("Held", self.held_piece.coords, self.held_piece.color)
        board = TetrisBoardBlock("Board", self.board.copy(), self.current_piece.coords, self.current_piece.color)
        data = TetrisData(next, held, board)
        return self.display_with(data)

    def display_with(self, data: TetrisData):
        size = 6
        dx = -2
        dy = 2

        next = data.next
        next_block = np.zeros((size, size, 3), dtype=np.uint8)
        next_block[next.coords[:, 0] + dy, next.coords[:, 1] + dx] = next.color.value
        next_block = self.enlarge(next_block)

        held = data.held
        held_block = np.zeros((size, size, 3), dtype=np.uint8)
        held_block[held.coords[:, 0] + dy, held.coords[:, 1] + dx] = held.color.value
        held_block = self.enlarge(held_block)

        board = data.board
        board_block = board.src
        board_block[board.coords[:, 0], board.coords[:, 1]] = board.color.value
        board_block = self.enlarge(board_block)

        self.display_next(next.title, next_block)
        self.display_held(held.title, held_block)
        self.display_board(board.title, board_block)

        with self.condition:
            self.condition.wait(0.4)
        key = self.key_buffer.get()
        print(key)
        return key
