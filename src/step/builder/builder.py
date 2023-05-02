from .finder import Finder


class Builder:
    def __init__(self, path: str):
        self.path = path

    def build(self, path: str = None) -> tuple:
        if path is None:
            path = self.path
        with open(path, "r") as source:
            lines = source.readlines()
            dataset = [(lineno, line.strip("\n").strip("\t").strip()) for lineno, line in enumerate(lines, start=1)]
            source.close()
        finder = Finder(dataset)
        const = finder.find_const()
        settings = finder.find_settings()
        steps = finder.find_steps()

        return const, settings, steps
