from step.runner.filerunner import Runner


class FileParser:
    def __init__(self, args: list = None):
        self.args = args
        self.runner = None
        self.source = None

    def parse(self, args: list = None) -> Runner:
        if args is None:
            args = self.args
        source = args[-1]
        self.source = source
        return Runner(source)
