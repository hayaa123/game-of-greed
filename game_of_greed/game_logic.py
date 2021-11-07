import random


class GameLogic:
    @staticmethod
    def calculate_score(tup):
        """
        a function that accept a tuple as an input and return a calculated points for the greedy game 
        
        """
        total = 0
        pairs = 0
        tries = 0 

        list1 = [0, 100, 200, 1000, 2000, 3000, 4000]
        count1 = tup.count(1)

        if count1 ==3 :
            tries +=1
        elif count1 ==2 :
            pairs+=1
        
        

        list2 = [0, 0, 0, 200, 400, 600, 800]
        count2 = tup.count(2)
        if count2 ==3 :
            tries +=1
        elif count2 ==2 :
            pairs+=1

        list3 = [0, 0, 0, 300, 600, 900, 1200]
        count3 = tup.count(3)
        if count3 ==3 :
            tries +=1
        elif count3 ==2 :
            pairs+=1

        list4 = [0, 0, 0, 400, 800, 1200, 1600]
        count4 = tup.count(4)
        if count4 ==3 :
            tries +=1
        elif count4 ==2 :
            pairs+=1

        list5 = [0, 50, 100, 500, 1000, 1500, 2000]
        count5 = tup.count(5)
        if count5 ==3 :
            tries +=1
        elif count5 ==2 :
            pairs+=1

        list6 = [0, 0, 0, 600, 1200, 1800, 2400]
        count6 = tup.count(6)
        if count6 ==3 :
            tries +=1
        elif count6 ==2 :
            pairs+=1

        if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 == 1:
            return 1500

        elif pairs==3:
            return 1500
        elif tries == 2 :
            return 1200
        else:
            total = list1[count1] + list2[count2] + list3[count3] + list4[count4]+list5[count5] + list6[count6]

        return total
    @staticmethod
    def roll_dice(val):
        list =[]
        for i in range(val):
            list.append(random.randint(1,6))
        return tuple(list)