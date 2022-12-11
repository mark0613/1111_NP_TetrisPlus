class Task:
    def __init__(self, process, args=tuple()):
        self.process = process
        self.args = args
    
    def run(self):
        self.process(*self.args)
