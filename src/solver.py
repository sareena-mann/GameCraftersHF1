from game.template import Game, Value
from dataclasses import dataclass


@dataclass
class SolutionRecord:
    """
    Data regarding a specific position in a sequential game.
    """

    value: Value


class Solver:

    @staticmethod
    def solve(game: Game) -> dict[int, SolutionRecord]:
        """
        By exhaustively exploring all positions reachable in the provided game,
        returns a mapping of their encodings to their game-theoretic values in
        a dictionary (and other information we may care about).
        """

        # TODO: Homefun 1, Homefun 2
        ...
