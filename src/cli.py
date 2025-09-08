from dataclasses import dataclass
from solver import SolutionRecord
from enum import Enum
import sys


HELP_STRING = "Usage: main.py <game name> [arg1] [arg2] ..."


class GameImplementation(Enum):
    """
    The names of all available game implementations.
    """

    zero_by = 1


@dataclass
class Args:
    """
    Execution arguments for the program, specifying which game to solve and
    providing optional input for its initialization.
    """

    game: GameImplementation
    input: list[str]


class Cli:
    """
    Helper class for handling I/O through a command-line interface.
    """

    @staticmethod
    def success() -> None:
        sys.exit(0)

    @staticmethod
    def error(msg: str) -> None:
        print(msg)
        sys.exit(1)

    @staticmethod
    def parse() -> Args:
        if len(sys.argv) < 2:
            Cli.error(HELP_STRING)

        try:
            parsed_args = Args(
                game=GameImplementation[sys.argv[1]],
                input=sys.argv[2:]
            )

        except KeyError:
            Cli.error(f"Could not find game with name '{sys.argv[1]}'")

        return parsed_args

    @staticmethod
    def format(solution: dict[int, SolutionRecord]) -> None:
        Cli.__format_individual(solution)
        Cli.__format_aggregate(solution)

    @staticmethod
    def __format_individual(solution: dict[int, SolutionRecord]) -> None:

        # TODO: Homefun 1
        ...

    @staticmethod
    def __format_aggregate(solution: dict[int, SolutionRecord]) -> None:

        # TODO: Homefun 2, Homefun 3
        ...
