import random
from wordle import Game, LetterStates

class RobotPlayer:
    ASSUME_GUESSES_VALID = True

    PRESETS = ["FILES", "PRANG"]

    def __init__(self, valid_guesses: tuple, valid_solutions: tuple):
        self._all_words = valid_guesses
        self._valid_solutions = valid_solutions

        self.response_history = []
        self._possible_solutions = []
        self._guessed_words = set()
        self.common_guesses = [
            {guess: 0 for guess in self._all_words} for _ in range(Game.ROUNDS)
        ]

    def start(self):
        self.response_history = []
        self._possible_solutions = [word for word in self._valid_solutions]
        self._guessed_words = set()

    def guess(self, round) -> str:
        if round <= len(self.PRESETS) and len(self._possible_solutions) > 20:
            guess = self.PRESETS[round - 1]
        elif len(self._possible_solutions) == 1 or round >= Game.ROUNDS:
            guess = self._possible_solutions[0]
        else:
            guess = self.minimax_guess()

        self.common_guesses[round - 1][guess] += 1
        return guess

    def minimax_guess(self):
        scores = {}
        count_possible_solutions = len(self._possible_solutions)
        max_solutions = min(count_possible_solutions, 20)
        max_guesses = min(len(self._all_words), 1000 // max_solutions)

        # For every possible guess
        for guess in set(self._possible_solutions + random.sample(self._all_words, k=max_guesses)):
            if guess in self._guessed_words:
                continue
            min_eliminated = count_possible_solutions
            # Test possible guess against every possible solution
            for possible_solution in random.sample(self._possible_solutions, k=max_solutions):
                states = Game.check_guess(guess, possible_solution)
                eliminated = 0
                # Count number of possible solutions that would be eliminated by the guess, if the true solution was possible_solution
                for s in random.sample(self._possible_solutions, k=max_solutions):
                    if not Game.is_same_response(guess, s, states):
                        eliminated += 1
                if eliminated < min_eliminated:
                    min_eliminated = eliminated
                if min_eliminated == 0:
                    break  # no need to test against further possible solutions if min eliminated already zero
            scores[guess] = min_eliminated

        max_score = max(scores.values())
        best_guesses = [guess for guess, score in scores.items() if score == max_score]
        if len(best_guesses) == 1:
            return best_guesses[0]

        # if more than one best guess, sort alphabetically and return first one (ensures guesses are deterministic)
        # prefer a best guess which is a possible solution
        best_guesses = sorted(best_guesses)
        for best_guess in best_guesses:
            if best_guess in self._possible_solutions:
                return best_guess
        return best_guesses[0]

    def handle_response(self, guess: str, states: list[LetterStates]):
        self.response_history.append((guess, states))
        if states == Game.WIN_STATES:
            return

        self._guessed_words.add(guess)
        self._possible_solutions = [
            possible_solution
            for possible_solution in self._possible_solutions
            if all(Game.is_same_response(guess, possible_solution, states) for guess, states in self.response_history)
        ]
