import sys
from step import StepFrameWork


def run_cli():
    args = sys.argv[1:]
    StepFrameWork().run(args)
