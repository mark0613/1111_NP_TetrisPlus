import threading


class KeyBuffer:
    def __init__(self, limit=1):
        self.buffer = -1
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    def get(self) -> int:
        self.lock.acquire()
        data = self.buffer
        self.buffer = -1
        self.lock.release()
        return data

    def put(self, key: int):
        self.lock.acquire()
        self.buffer = key
        self.lock.release()
