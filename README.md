# Homefun Template 

Python aid for completing the Gamescrafters Homefun series. Incomplete functions are marked `# TODO`, but just completing these functions may not be sufficient. You are encouraged to change any module as you see fit.

## Requirements

You will need:
* Python 3.8+
* The `make` program
* A unix-like environment (Windows users, see Git Bash or WSL)

## Usage 

The program is a barebones CLI application that lets you specify which game you want to solve and to pass inputs to your game initializers. For example, once you complete Homefun 1, the following command:

```
make run ARGS="zero_by 25 1 3 4"
```

...should result in a solution to 25-to-0-by-1-3-or-4; the string `zero_by` told the program which game to solve, and `25 1 3 4` allowed us to specify arguments for the game's parameters. 

## Testing

There are no tests included, but you are encouraged to write your own in the provided `src/tests.py` file. As a suggestion, a useful test is comparing the solver output to the expected output. You can run them as follows:

```
make test
```

## Using Other Languages

For those comfortable in their programming ability, this series is a great opportunity to learn a new programming language. If you wish to not use Python, you are free to complete the assignments however you would like.

To do this, you can simply make a commit deleting everything in the repository that is not useful to your code. Just ensure that the following holds when you are finished:

* Running `make run ARGS="..."` works from the project directory
* The output of your program is identical to the required output

To do this, you may have to add a compilation step to `make run`.

