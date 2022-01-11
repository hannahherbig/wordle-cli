Command-line clone of Josh Wardle's [Wordle](https://www.powerlanguage.co.uk/wordle/), inspired by [Paul Battley's Ruby version](https://github.com/threedaymonk/wordle). Features:

- play against random solutions, or against the once-a-day "official" Wordle solution (with `--today`)
- official dictionaries of solutions and valid guesses
- spoiler-free emoji summaries for sharing

![Screenshot of a Wordle CLI game](/assets/screenshot.png?raw=true "Screenshot of a Wordle CLI game")

### Solving Wordle

Using a combination of [Knuth's minimax algorithm for Mastermind](<https://en.wikipedia.org/wiki/Mastermind_(board_game)#Worst_case:_Five-guess_algorithm>) and two hardcoded initial guesses, it's possible to win Wordle for 100% of possible solutions. The algorithm is seeded with the "offical" list of valid guesses (_not_ the solutions). This is effectively available to human players as well (as the game rejects invalid words without using up a guess). This repo contained a solver, but it was unnecessarily slow, so I'm rewriting it and will release in due course.

### Download and run (`./play.py`)

Requires **Python 3.6** or later, and a **modern terminal app** (e.g. [Windows Terminal](https://aka.ms/terminal) if running Windows)

To get the code:

```
git clone https://github.com/klipspringr/wordle-cli.git && cd wordle-cli
```

alternatively, if you don't have git: click `Code > Download ZIP` on GitHub, extract the ZIP, open a terminal and `cd` to the extracted folder.

To run on **Linux** or **WSL**:

```
./play.py
```

To run on **Windows**:

```
python3 play.py
```

A terminal with colour and emoji support is required. On Windows and WSL, [Windows Terminal](https://aka.ms/terminal) is the best choice. PowerShell and the Windows command prompt are only supported if running in Windows Terminal.

Not tested on **macOS**, but should work &mdash; let me know if any problems!

### Options

Usage: `./play.py [-h|--help|--today|SOLUTION]`

| Argument        | Behaviour                                                 |
| --------------- | --------------------------------------------------------- |
| _none_          | Use a random solution from the official Wordle dictionary |
| `-h` , `--help` | Print this help text and quit                             |
| `--today`       | Use today's official Wordle solution                      |
| `SOLUTION`      | Use a given SOLUTION (probably only useful for debugging) |

### Config file

To tweak the terminal colours and other variables, copy `config.ini.defaults` to `config.ini` and uncomment and edit the relevant lines. Colours are specified using ECMA-48 Select Graphic Rendition codes ([cheat sheet](https://i.stack.imgur.com/6otvY.png)).
