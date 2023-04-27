class SettingBuilder:
    dataset = None
    stat_line = None
    end_line = None

    def __init__(self, dataset: list, start_line: int, end_line: int):
        self.dataset = dataset
        self.stat_line = start_line
        self.end_line = end_line
