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
        if current in Solver.sol:
            #print(f"{current} : {Solver.sol[current].value}")
            #return Solver.sol[current].value
            return

        next_moves = game.get_moves(current)
        if not next_moves:
            val = game.terminal_value(current)
        else:
            # Solve children first (post-order traversal)
            child_values = [Solver.solve_helper(n, game) for n in next_moves]
            val = Value.WIN if any(v == Value.LOSE for v in child_values) else Value.LOSE

        Solver.sol[current] = SolutionRecord(value=val)
        print(f"{current}: {val.value}")
        return val
"""
    @staticmethod
    def solve_helper(current, game):
        next = game.get_moves(current)
        if current in Solver.sol:
            print(f"{current} : {Solver.sol[current].value}")

        else:
            Solver.sol[current] = game.terminal_value(current)

        #Solve Children First
        for n in next:
            Solver.solve_helper(n, game)

        print(f"{current}: {Solver.sol[current].value}")
"""