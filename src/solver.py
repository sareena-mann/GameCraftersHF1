from game.template import Game, Value
from dataclasses import dataclass
@dataclass
class SolutionRecord:
    """
    Data regarding a specific position in a sequential game.
    """

    value: Value

class Solver:
    sol: dict[int, SolutionRecord] = {}

    @staticmethod
    def solve(game: Game) -> dict[int, SolutionRecord]:
        """
        By exhaustively exploring all positions reachable in the provided game,
        returns a mapping of their encodings to their game-theoretic values in
        a dictionary (and other information we may care about).
        """
        #Solver.sol.clear()
        start_position = game.start()
        Solver.solve_helper(start_position, game)
        return Solver.sol

    @staticmethod
    def solve_helper(current, game):
        next = game.get_moves(current)
        Solver.sol[current] = game.terminal_value(current)
        if not next:
            val = game.terminal_value(current)
            Solver.sol[current] = SolutionRecord(val)
            print(f"{current}: {val.value}")
            return

        #Solve Children First
        for n in next:
            if n not in Solver.sol:
                Solver.solve_helper(n, game)

        print(f"{current}: {Solver.sol[current].value}")
