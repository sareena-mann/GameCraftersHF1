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
        Solver.sol.clear()
        Solver.solve_helper(game.start(), game)
        return Solver.sol

    @staticmethod
    def solve_helper(current, game):
        if current in Solver.sol:
            return Solver.sol[current].value

        val = game.terminal_value(current)
        if val is not None:
            Solver.sol[current] = SolutionRecord(val)
            return val

        next_moves = game.get_moves(current)
        for n in next_moves:
            next_pos = game.do_move(current, n)
            next_val = Solver.solve_helper(next_pos, game)
            if next_val.value == "LOSE":
                Solver.sol[current] = SolutionRecord(Value("WIN"))
                return Value("WIN")

        Solver.sol[current] = SolutionRecord(Value("LOSE"))
        return Value("LOSE")