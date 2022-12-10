from .config import *

from enum import Enum
import cv2
import numpy as np
import random


class PieceType(Enum):
    I = [[0, 3], [0, 4], [0, 5], [0, 6]]
    T = [[1, 3], [1, 4], [1, 5], [0, 4]]
    L = [[1, 3], [1, 4], [1, 5], [0, 5]]
    J = [[1, 3], [1, 4], [1, 5], [0, 3]]
    S = [[1, 5], [1, 4], [0, 3], [0, 4]]
    Z = [[1, 3], [1, 4], [0, 4], [0, 5]]
    O = [[0, 4], [0, 5], [1, 4], [1, 5]]

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, PieceType):
            return self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Piece:
    def __init__(self, type: PieceType, color: Color, coords=None):
        self.type = type
        self.color = color
        if coords is None:
            self.coords = type.value
        else:
            self.coords = coords

class TetrisCommand(Enum):
    ROTATE = ord('w')
    LEFT = ord('a')
    RIGHT = ord('d')
    HARD_DROP = 32  # space
    HOLD = ord('q')
    QUIT = 27  # esc
    OTHER = 0

    @classmethod
    def get_type(cls, key: int):
        if key < 0:
            return TetrisCommand.OTHER
        key = ord(chr(key).lower())
        for c in TetrisCommand:
            if c.value == key:
                return c
        return TetrisCommand.OTHER

class Tetris:
    def __init__(self, ratio: int=20):
        self.ratio = ratio
        self.level = 2
        self.score = 0
        self.piece_code = [piece for piece in PieceType]
        self.piece_color = {
            PieceType.I : Color.WHITE,
            PieceType.T : Color.PURPLE,
            PieceType.L : Color.PINK,
            PieceType.J : Color.BLUE,
            PieceType.S : Color.GREEN,
            PieceType.Z : Color.RED,
            PieceType.O : Color.YELLOW, 
        }
        self.board = np.zeros((20, 10, 3), dtype=np.uint8)

        self.is_gaming = True
        self.is_placed = False
        self.is_hard_drop = False
        self.switch = False
        self.current_piece_type = None
        self.held_piece_type = None
        self.next_piece_type = self.get_random_piece_type()
        self.current_piece = None
        self.held_piece = None
        self.next_piece = None

    def get_random_piece_type(self) -> PieceType:
        return random.choice(self.piece_code)

    def get_empty_piece(self):
        return Piece(None, Color.BLACK, np.array([[0, 0]]))

    def get_piece(self, piece_type: PieceType) -> Piece:
        if piece_type is None:
            return self.get_empty_piece()
        color = self.piece_color[piece_type]
        piece = Piece(piece_type, color)
        piece.coords = np.array(piece.coords)
        return piece

    def eliminate(self):
        lines = 0
        for line in range(20):
            if np.all([np.any(pos != 0) for pos in self.board[line]]):
                lines += 1
                self.board[1:line+1] = self.board[:line]
        if lines == 0:
            return

        if lines == 1:
            self.score += 40
        elif lines == 2:
            self.score += 100
        elif lines == 3:
            self.score += 300
        elif lines == 4:
            self.score += 1200

    def switch_pieces(self):
        if self.switch:
            self.held_piece_type, self.current_piece_type = self.current_piece_type, self.held_piece_type
            self.switch = False
        else:
            self.current_piece_type = self.next_piece_type
            self.next_piece_type = self.get_random_piece_type()

    def enlarge(self, array: np.ndarray, ratio: int =-1):
        if ratio < 0:
            ratio = self.ratio
        return array.repeat(ratio, 0).repeat(ratio, 1)

    def display(self):
        size = 6
        dx = -2
        dy = 2

        next_block = np.zeros((size, size, 3), dtype=np.uint8)
        next_block[self.next_piece.coords[:, 0] + dy, self.next_piece.coords[:, 1] + dx] = self.next_piece.color.value
        next_block = self.enlarge(next_block)

        held_block = np.zeros((size, size, 3), dtype=np.uint8)
        held_block[self.held_piece.coords[:, 0] + dy, self.held_piece.coords[:, 1] + dx] = self.held_piece.color.value
        held_block = self.enlarge(held_block)

        board_block = self.board.copy()
        board_block[self.current_piece.coords[:, 0], self.current_piece.coords[:, 1]] = self.current_piece.color.value
        board_block = self.enlarge(board_block)

        cv2.imshow("Next", next_block)
        cv2.imshow("Held", held_block)
        cv2.imshow("Board", board_block)
        return cv2.waitKey(1000 / self.level)

    def on_listen_key(self, key: int):
        coords = self.current_piece.coords
        key = TetrisCommand.get_type(key)
        if key is TetrisCommand.LEFT:
            if np.min(coords[:,1]) > 0:
                coords[:,1] -= 1
            if self.current_piece_type is PieceType.I:
                self.top_left[1] = 0 if self.top_left[1]<1 else self.top_left[1]-1
        
        elif key is TetrisCommand.RIGHT:
            if np.max(coords[:,1]) < 9:
                coords[:,1] += 1
                if self.current_piece_type is PieceType.I:
                    self.top_left[1] += 1
        
        elif key is TetrisCommand.ROTATE:
            if not (self.current_piece_type is PieceType.I) and not(self.current_piece_type is PieceType.O):
                if coords[1,1] > 0 and coords[1,1] < 9:
                    self.arr = coords[1] - 1 + np.array([[[x, y] for y in range(3)] for x in range(3)])
                    self.pov = coords - coords[1] + 1
            elif self.current_piece_type is PieceType.I:
                self.arr = self.top_left + np.array([[[x, y] for y in range(4)] for x in range(4)])
                self.pov = np.array([np.where(np.logical_and(self.arr[:,:,0] == pos[0], self.arr[:,:,1] == pos[1])) for pos in coords])
                self.pov = np.array([k[0] for k in np.swapaxes(self.pov, 1, 2)])
            if not (self.current_piece_type is PieceType.O):
                self.arr = np.rot90(self.arr, -1)
                coords = self.arr[self.pov[:,0], self.pov[:,1]]
            self.current_piece.coords = coords
        
        elif key is TetrisCommand.HARD_DROP:
            self.is_hard_drop = True
        
        elif key is TetrisCommand.HOLD:
            if self.held_piece_type is None:
                self.held_piece_type = self.current_piece_type
            else:
                self.switch = True
            return True
        
        elif key is TetrisCommand.QUIT:
            self.is_gaming = False
            return True
        
        return False

    def adjust_piece_position(self, dummy: np.ndarray):
        coords = self.current_piece.coords
        if np.all(coords[:,0] < 20) and np.all(coords[:,0] >= 0):
            if self.current_piece_type is PieceType.I and (np.all(coords[:,1] >= 10)  or np.all(coords[:,1] < 0)):
                coords = dummy.copy()
            else:
                if np.any(self.board[coords[:,0], coords[:,1]] != 0):
                    coords = dummy.copy()
        else:
            coords = dummy.copy()
        self.current_piece.coords = coords

    def play(self):
        while self.is_gaming:
            self.switch_pieces()
            
            self.held_piece = self.get_piece(self.held_piece_type)
            self.next_piece = self.get_piece(self.next_piece_type)
            self.current_piece = self.get_piece(self.current_piece_type)

            if self.current_piece_type is PieceType.I:
                self.top_left = [-2, 3]

            coords = self.current_piece.coords
            color = self.current_piece.color.value
            if np.any(self.board[coords[:, 0], coords[:, 1]] != 0):
                break

            while True:
                key = self.display()
                dummy = coords.copy()

                break_loop = self.on_listen_key(key)
                if break_loop:
                    break
                self.adjust_piece_position(dummy)
                coords = self.current_piece.coords

                if self.is_hard_drop:
                    while not self.is_placed:
                        if np.all(coords[:, 0] < 19):  # 放在其他方塊上
                            for (y, x) in coords:
                                if not np.array_equal(self.board[y + 1, x], Color.BLACK.value):
                                    self.is_placed = True
                                    break
                        else:  # 放在地上
                            self.is_placed = True

                        if self.is_placed:
                            break

                        coords[:, 0] += 1
                        if self.current_piece_type is PieceType.I:
                            self.top_left[0] += 1
                    self.is_hard_drop = False
                else:
                    if np.all(coords[:, 0] < 19):  # 放在其他方塊上
                        for (y, x) in coords:
                            if not np.array_equal(self.board[y + 1, x], Color.BLACK.value):
                                self.is_placed = True
                                break
                    else:  # 放在地上
                        self.is_placed = True
                
                if self.is_placed:
                    for (y, x) in coords:
                        self.board[(y, x)] = color
                    self.is_placed = False
                    break

                coords[:, 0] += 1
                if self.current_piece_type is PieceType.I:
                    self.top_left[0] += 1
            
            self.eliminate()
        self.end_game()

    def end_game(self):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()
