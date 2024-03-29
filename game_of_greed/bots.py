"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""

import builtins
import re
from abc import abstractmethod

from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0
        self.rolled_dice = ()
        

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"Congrats! {num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class AmmanBot(BasePlayer):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.rolled_dice = ()

    def _mock_print(self, *args):
        self.old_print(*args)
        printed_data = str(args[0])
        if printed_data[0].isdigit():
            self.rolled_dice = tuple(int(ch) for ch in printed_data.split(','))

    def _mock_input(self, *args):
        self.old_print(*args)
        self.old_print(self.total_score)

        if args[0].startswith('Wanna play'):
            return 'y'

        elif self.total_score > 1000 and args[0].startswith('Enter dice'):
            return 'q'

        elif args[0].startswith('Enter dice'):
            return "".join([str(i) for i in self.rolled_dice])
          
        elif args[0].startswith('(r)oll again, (b)ank your points or (q)ui'):
            self.total_score += GameLogic.calculate_score(self.rolled_dice)
            return 'b'
       
if __name__=="__main__":
    # bot1 = BasePlayer()
    # bot1.play()
    amman_bot = AmmanBot()
    amman_bot.play(3)