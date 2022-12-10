from src.game.data_format import *
from src.game.keyboard import KeyBuffer
from src.game.tetris import Tetris
from src.utils.tasks import Task

import threading


class MyTetris(Tetris):
    def __init__(self, ratio=20, send_data=None):
        super().__init__(ratio)
        self.send_data = send_data

    def set_key_buffer(self, key_buffer: KeyBuffer):
        self.key_buffer = key_buffer
    
    def set_condition(self, condition: threading.Condition):
        self.condition = condition

    def set_display_method(self, next, held, board):
        self.display_next = next
        self.display_held = held
        self.display_board = board

    def set_show_score_method(self, show):
        self.show_score = show

    def set_end_game_tasks(self, tasks: list):
        self.end_tasks = tasks

    def display(self):
        self.show_score(self.score)
        next = TetrisSmallBlock("Next", self.next_piece.coords, self.next_piece.color)
        held = TetrisSmallBlock("Held", self.held_piece.coords, self.held_piece.color)
        board = TetrisBoardBlock("Board", self.board.copy(), self.current_piece.coords, self.current_piece.color)
        data = TetrisData(next, held, board)
        if self.send_data:
            self.send_data(str(data))
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

        if hasattr(self, "condition"):
            with self.condition:
                self.condition.wait(1 / self.level)
            key = self.key_buffer.get()
            print(key)
            return key

    def end_game(self):
        if hasattr(self, "end_tasks"):
            for task in self.end_tasks:
                task.run()
