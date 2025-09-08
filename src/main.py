from cli import Cli, Args, GameImplementation
from solver import Solver, SolutionRecord
from game.zero_by import ZeroBy


if __name__ == "__main__":

    arguments: Args = Cli.parse()
    solution: dict[int, SolutionRecord] = {}

    match arguments.game:
        case GameImplementation.zero_by:
            game = ZeroBy(arguments.input)
            solution = Solver.solve(game)

    Cli.format(solution)
    Cli.success()
