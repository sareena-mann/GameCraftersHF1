from game.template import Game, Value

class ZeroBy(Game):

    def __init__(self, args: list[str]):
        # Example: ARGS="zero_by 10 1 2"
        self.args = args
        self.steps = args[1:]

    def start(self) -> int:
        return int(self.args[0])

    def get_moves(self, position: int) -> list[int]:
        # Explore all possible places to go one step down from current position
        moves: list[int] = []
        for i in self.steps:
            if int(i) <= position:
                moves.append(position - int(i))
        return moves

    def do_move(self, position: int, move: int) -> int:
        if move <= position:
            return position - move
        return 0

    def terminal_value(self, position: int) -> Value:
        # get_moves and check: All W children --> LOSE  // at least 1 L children --> WIN
        outcomes = self.get_moves(self, position)
        for pos in outcomes:
            if pos == Value.LOSE:
                return Value.WIN
        return Value.LOSE
