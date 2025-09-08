from abc import ABC, abstractmethod
from enum import Enum


class Value(Enum):
    """
    Indicates the value of a terminal position in a sequential game.

    The notion of value we are using here is non-formal, but intuitively, we
    assume that players seek to always WIN, TIE where they cannot, and that
    they LOSE in all other cases.

    You will notice there is a MEDIAL option that is not like the rest. This
    is here to make it more straightforward to implement `Game.get_moves`,
    which is only defined for medial (non-terminal) positions. This is part of
    what ensures that solving algorithms which consume the `Game` Interface
    terminate. If you can ensure this in some other way, feel free to remove
    the MEDIAL enum variant.
    """

    WIN = "WIN"
    TIE = "TIE"
    LOSE = "LOSE"
    MEDIAL = "MEDIAL"


class Game(ABC):
    """
    Interface sequential, deterministic, complete-information games.
    """

    @abstractmethod
    def start(self) -> int:
        """
        Returns an encoding of a game's starting position.
        """
        pass

    @abstractmethod
    def get_moves(self, position: int) -> list[int]:
        """
        Given a position encoding, returns a list of encodings corresponding
        to moves that can be done from the provided position.

        Warning: In most implementations, this function should only be defined
        in a domain of positions that are non-terminal. This may not apply to
        your implementation, however.
        """
        pass

    @abstractmethod
    def do_move(self, position: int, move: int) -> int:
        """
        Given a position encoding and a move encoding, returns the encoding of
        the position that would result if the provided move was done from the
        provided position.
        """
        pass

    @abstractmethod
    def terminal_value(self, position: int) -> Value:
        """
        Returns the value of the provided position if it is terminal, and None
        in all other cases.
        """
        pass
