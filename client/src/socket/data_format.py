from src.game.config import *

import json
import numpy as np


class TetrisBlock:
    def __init__(self, title: str, coords: np.ndarray, color: Color) -> None:
        self.title = title
        self.coords = coords
        self.color = color
        self.set_data()
    
    @classmethod
    def load_by_string(cls, data: str):
        data = json.loads(data)
        data["coords"] = np.array(data["coords"])
        data["color"] = Color[data["color"]]
        return TetrisBlock(**data)

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

class TetrisData:
    def __init__(self, next: TetrisBlock, held: TetrisBlock, board: TetrisBlock) -> None:
        self.next = next
        self.held = held
        self.board = board
    
    def __str__(self) -> str:
        data = self.__dict__.copy()
        for k, v in data.items():
            data[k] = v.get_json_data("transport")
        return json.dumps(data)

    def get_json_data(self) -> dict:
        data = self.__dict__.copy()
        for k, v in data.items():
            data[k] = v.get_json_data()
        return data
