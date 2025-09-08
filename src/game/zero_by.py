from game.template import Game, Value


class ZeroBy(Game):

    def __init__(self, args: list[str]):
        self.args = args

    def start(self) -> int:

        # TODO: Homefun 1
        ...

    def get_moves(self, position: int) -> list[int]:

        # TODO: Homefun 1
        ...

    def do_move(self, position: int, move: int) -> int:

        # TODO: Homefun 1
        ...

    def terminal_value(self, position: int) -> Value:

        # TODO: Homefun 1
        ...
