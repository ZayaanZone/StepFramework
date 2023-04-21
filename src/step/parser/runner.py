import os


class Runner:
    def __init__(self, source: str):
        self.source = source

    def run(self):
        path = os.path.abspath(self.source)
        print(path)
