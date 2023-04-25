__doc__ = """
A python module to run tests as steps
"""
__version__ = "0.1.0"
__author__ = "Sanaur Asif"
__email__ = "sanaurasif2@gmail.com"

from step.parser.fileparser import FileParser


class StepFrameWork:
    def __int__(self, args: list = None):
        self.args = args

    def parse_args(self, args: list = None):
        if args is None:
            args = self.args
        _parser = FileParser(args)
        return _parser.parse()

    def run(self, args: list = None):
        if args is None:
            args = self.args
        runner = self.parse_args(args)
        return runner.run()
