from game.template import Game, Value

class ZeroBy(Game):
    def __init__(self, args: list[str]):
        self.args = args
        self.steps = args[1:]

    def start(self) -> int:
        return int(self.args[0])

    def get_moves(self, position: int) -> list[int]:
        return [int(s) for s in self.steps if int(s) <= position]

    def do_move(self, position: int, move: int) -> int:
        if position >= move:
            return position - move
        return 0

    def terminal_value(self, position: int) -> Value:
        if position == 0:
            return Value.LOSE
        return None
