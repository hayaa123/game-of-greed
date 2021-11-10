from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter


class Game:
    def __init__(self, roller=None):
        self.roller = roller or   GameLogic.roll_dice

    def play(self):
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
        if wanna_play == 'n':
            print('OK. Maybe another time')

        else:
            round = 1
            banker = Banker()
            flag = True
            flagrolling = True
            zilch = 0
            counrRoll=6
            while flag:
                if flagrolling == True:
                    print(f'Starting round {round}')
                print(f'Rolling {counrRoll} dice...')
                rolled_dice = self.roller(counrRoll)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
               

                # should repeate while cheating
                
                cheating =True
                decision = ""
                while cheating :
                    zilch = GameLogic.calculate_score([int(i) for i in nums])
                    print(','.join(nums))
                    if zilch == 0:
                        print("Zilch!!! Round over")
                        print(f'You banked 0 points in round {round}\nTotal score is 0 points')
                        round += 1
                        print(f"Starting round {round}\nRolling 6 dice...")
                        print(','.join(nums)) 
                    decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                    list_desision = [i for i in decision] 
                    if decision == "q":
                        break
                    
                    for i in list(set(list_desision)):
                        if nums.count(i) >= list_desision.count(i):
                            cheating = False
                            
                        else : 
                            print("Cheater!!! Or possibly made a typo...")
                            cheating = True

                if decision == "q":
                    # print('hhhhhhhhhhhh')
                    if round == 1 and banker.shelved == 0:
                        print(f'Thanks for playing. You earned {banker.balance} points')
                        flag = False
                    else:
                        print(f'Total score is {banker.balance} points')
                        print(f'Thanks for playing. You earned {banker.balance} points')
                        flag = False

                else:
              
                    banker.shelf(GameLogic.calculate_score(tuple([int(i) for i in decision])))
                   
                    print(
                        f'You have {banker.shelved} unbanked points and { 6 - len(decision)} dice remaining')
                    bankpoints = input(
                        '(r)oll again, (b)ank your points or (q)uit ')
                    if bankpoints == 'q':
                        print(f'Total score is {banker.balance} points')
                        print(f'Thanks for playing. You earned {banker.balance} points')
                        flag = False
                    if bankpoints == 'b':
                        counrRoll = 6
                        print(f'You banked {banker.shelved} points in round {round}')
                        banker.bank()
                        banker.clear_shelf()
                        print(f'Total score is {banker.balance} points')
                        round += 1
                        flagrolling = True
                    if bankpoints == 'r':
                        flagrolling = False
                        counrRoll -= len(decision)
                        continue


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
