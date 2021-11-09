from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter


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
            banker = Banker()
            flag = True
            flagrolling = True

            while flag:
                if flagrolling == True:
                    print(f'Starting round {round}')
                print('Rolling 6 dice...')
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))


                # should repeate while cheating
                
                print(','.join(nums))
                
                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                # parsed_desios = Counter([i for i in decision])
                # nums2 =Counter(nums)
                # print(parsed_desios)
                # {5:2,3:1,2:2,4:1}
                # {5:3}
                # [2,2,1,1]
                # keyslist = list(parsed_desios.keys()) ==> "5"
                # nums2[keyslist[0]] == 2
                # parsed_desios[keyslist[0]]== 3
                # should be false 
                #__________________________________-
                list_desision = [i for i in decision] 
                #nums is already a list 
                for i in list(set(list_desision)):
                    if nums.count(i) >= list_desision.count[i]:
                        continue
                    else : 
                        print("Cheater!!! Or possibly made a typo...")
                        break  


                if decision == "q":
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
                    if bankpoints == 'b':
                        print(f'You banked {banker.shelved} points in round {round}')
                        banker.bank()
                        banker.clear_shelf()
                        print(f'Total score is {banker.balance} points')
                        round += 1
                        flagrolling = True
                    if bankpoints == 'r':
                        flagrolling = False
                        continue


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
