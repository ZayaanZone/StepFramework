import sys
from step import StepFrameWork


def run_cli(args: list = None):
    if args is None:
        args = sys.argv[1:]
    return StepFrameWork().run(args)
