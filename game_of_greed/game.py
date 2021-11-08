from game_of_greed.game_logic import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller
    def play(self):
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
        if wanna_play == 'n':
            print('OK. Maybe another time')
        else:
            round = 1
            print('Starting round 1')
            print('Rolling 6 dice...')
            rolled_dice = self.roller(6)
            nums = []
            
            for i in rolled_dice:
                nums.append(str(i))
            print(','.join(nums))
            decision = input('Enter dice to keep (no spaces), or (q)uit: ')
            # print(tuple([int(i) for i in decision]  ))

            points = (GameLogic.calculate_score(tuple([int(i) for i in decision]  ))) 

           
            print(f'You have {points} unbanked points and { 6 - len(decision)} dice remaining')

            bankpoints= input('(r)oll again, (b)ank your points or (q)uit ')
             
            if bankpoints == 'b':
                print(f'You banked {points} points in round {round}')
                print(f'Total score is {points} points')
                round += 1
                print(f'Starting round {round}')
                print(f'Rolling 6 dice...')
                rolled_dice = self.roller(6)
                nums = []
                
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                if decision== 'q':
                    print(f'Total score is {points} points')
                    print(f'Thanks for playing. You earned {points} points')



if __name__=="__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
    