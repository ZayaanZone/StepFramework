class Finder:
    def __init__(self, dataset: list = None):
        self.dataset = dataset
        self.lines = None
        self.const = None
        self.settings = None
        self.steps = None

    def find_const(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset
        const = []
        pass

    def find_settings(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset
        settings = []
        pass

    def find_steps(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset
        steps = []
        pass
