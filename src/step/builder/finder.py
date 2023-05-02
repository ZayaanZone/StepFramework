from .consts import ConstBuilder
from .settings import SettingBuilder
from .steps import StepBuilder


class Finder:
    def __init__(self, dataset: list = None):
        self.dataset = dataset
        self.lines = None
        self.const = None
        self.settings = None
        self.steps = None
        self.const_keyword = "*** Continous ***"
        self.settings_keyword = "*** Settings ***"
        self.steps_keyword = "*** Steps ***"

    def find_const(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset

        linenos = [lineno for lineno, data in dataset if data == self.const_keyword]
        linenosend = [
            lineno
            for lineno, data in dataset
            if data == self.settings_keyword or data == self.steps_keyword
        ]
        print(linenos, linenosend)

        if len(linenos) > 1:
            raise ValueError("Multiple Continous Declarations Found")
        elif not linenos:
            return None

        start_line = linenos[0]
        end_line = None

        for linenoend in linenosend:
            if linenoend > start_line:
                end_line = linenoend - 1
                break

        if end_line is None:
            end_line = len(dataset)

        const = ConstBuilder(dataset, start_line, end_line)
        return const

    def find_settings(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset

        linenos = [lineno for lineno, data in dataset if data == self.settings_keyword]
        linenosend = [
            lineno
            for lineno, data in dataset
            if data == self.const_keyword or data == self.steps_keyword
        ]

        if len(linenos) > 1:
            raise ValueError("Multiple Setting Declarations Found")
        elif not linenos:
            return None

        start_line = linenos[0]
        end_line = None

        for linenoend in linenosend:
            if linenoend > start_line:
                end_line = linenoend - 1
                break

        if end_line is None:
            end_line = len(dataset)

        settings = SettingBuilder(dataset, start_line, end_line)
        return settings

    def find_steps(self, dataset: list = None):
        if dataset is None:
            dataset = self.dataset

        linenos = [lineno for lineno, data in dataset if data == self.steps_keyword]
        linenosend = [
            lineno
            for lineno, data in dataset
            if data == self.const_keyword or data == self.settings_keyword
        ]

        if len(linenos) > 1:
            raise ValueError("Multiple Step Declarations Found")
        elif not linenos:
            return None

        start_line = linenos[0]
        end_line = None

        for linenoend in linenosend:
            if linenoend > start_line:
                end_line = linenoend - 1
                break

        if end_line is None:
            end_line = len(dataset)

        steps = StepBuilder(dataset, start_line, end_line)
        return steps
