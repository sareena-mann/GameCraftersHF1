from game.template import Game, Value
from dataclasses import dataclass


@dataclass
class SolutionRecord:
    """
    Data regarding a specific position in a sequential game.
    """
    value: Value
    sol: dict[int, value]


class Solver:

    @staticmethod
    def solve(game: Game) -> dict[int, SolutionRecord]:
        """
        By exhaustively exploring all positions reachable in the provided game,
        returns a mapping of their encodings to their game-theoretic values in
        a dictionary (and other information we may care about).
        """
        #Ex: make run ARGS="zero_by 10 1 2"
        current = game.start(game)
        Solver.solve_helper(current, game)

        #Think about memoizing later

    @staticmethod
    def solve_helper(current, game):
        # This is a recursive function that explores all game states
        next = game.get_moves(current)

        #Base Case
        if len(next) == 0:
            return

        for n in next:
            print(n + ": " + game.terminal_value(current))
            Solver.solve_helper(game.do_move(current, n))


    #Later implement memoize so you don[t have to re-compute