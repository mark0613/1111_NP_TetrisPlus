from src.game.config import *

import json
import numpy as np


class TetrisSmallBlock:
    def __init__(self, title: str, coords: np.ndarray, color: Color) -> None:
        self.title = title
        self.coords = coords
        self.color = color
        self.set_data()

    @classmethod
    def load_by_transport_format(cls, title: str, coords: list, color: str):
        return TetrisSmallBlock(title, np.array(coords), Color[color])

    def get_json_data(self, type: str="origin"):
        if type == "transport":
            return self.data
        data = self.__dict__.copy()
        data.pop("data", None)
        return data

    def __str__(self):
        return json.dumps(self.data)

    def set_data(self):
        self.data = self.__dict__.copy()
        self.data["coords"] = self.data["coords"].tolist()
        self.data["color"] = self.data["color"].name

class TetrisBoardBlock(TetrisSmallBlock):
    def __init__(self, title: str, src: np.ndarray, coords: np.ndarray, color: Color) -> None:
        self.src = src
        super().__init__(title, coords, color)
    
    @classmethod
    def load_by_transport_format(cls, title: str, src: list, coords: list, color: str):
        return TetrisBoardBlock(title, np.array(src), np.array(coords), Color[color])

    def set_data(self):
        super().set_data()
        self.data["src"] = self.data["src"].tolist()

class TetrisData:
    def __init__(self, next: TetrisSmallBlock, held: TetrisSmallBlock, board: TetrisBoardBlock) -> None:
        self.next = next
        self.held = held
        self.board = board
        self.score = 0
    
    def __str__(self) -> str:
        data = self.__dict__.copy()
        for k, v in data.items():
            try:
                data[k] = v.get_json_data("transport")
            except AttributeError:
                pass
        data.pop("data", None)
        return json.dumps(data)

    def get_json_data(self) -> dict:
        data = self.__dict__.copy()
        for k, v in data.items():
            data[k] = v.get_json_data()
        data.pop("data", None)
        return data

    @classmethod
    def load_by_string(cls, data: str):
        data = json.loads(data)
        data["next"] = TetrisSmallBlock.load_by_transport_format(**data["next"])
        data["held"] = TetrisSmallBlock.load_by_transport_format(**data["held"])
        data["board"] = TetrisBoardBlock.load_by_transport_format(**data["board"])
        score = data["score"]
        data.pop("score", None)
        t = TetrisData(**data)
        t.score = score
        return t
