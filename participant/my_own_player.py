import random
from . import participant as part
import glass_stepping_stones.game as r3


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('My team', 8)

        # Gather marble random info
        random.seed(1)   # when seed 1, computer plays first

        self.first_bet = True
        self.first_bet_prev_marbles = 0
        self.i_know_computer_declare = False
        self.computer_declare = None

        # re-init seed
        random.seed(1)

        # for glass stepping
        # pos = 0
        self.current_position = 0
        self.glass_answer = []



    def bet_marbles_strategy_com(self, my_current_marbles):  # return should be the number of marbles bet
        if (my_current_marbles > 7):
            temp = list(range(1, int(my_current_marbles / 4), 2))
            temp = temp[random.randint(0, len(temp) - 1)]
            temp += round((random.uniform(0, 70) + 30) / 100)
        else:
            temp = random.randint(0, my_current_marbles)
        return temp


    def declare_statement_strategy_com(self):
        answer = bool(round((random.uniform(0, 70) + 30) / 100))
        self.__statement = answer
        return answer



    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        # you can override this method in this sub-class
        # this method must contain 'self.initialize_params()' which is for initializing some essential variables
        # you can initialize what you define
        self.initialize_params()
        random.seed(1)
        temp = random.randint(0, 1)
        for _ in range(100):
            self.glass_answer.append(random.randint(0, 1))

        self.current_position = 0     # 추가!

        random.seed(1)
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        random.seed(1)

        if self.first_bet:
            self.first_bet_prev_marbles = playground_marbles.get_num_of_my_marbles(self)
            self.first_bet = False
            return 1
        else:
            current_marble = playground_marbles.get_num_of_my_marbles(self)
            if self.computer_declare:    # com always declare odd
                if current_marble % 2:
                    return current_marble - 1
                else:
                    return current_marble
            else:
                if current_marble % 2:
                    return current_marble
                else:
                    return current_marble - 1


    def declare_statement_strategy(self, playground_marbles):
        random.seed(1)
        if not self.i_know_computer_declare and not self.first_bet:
            current_marbles = playground_marbles.get_num_of_my_marbles(self)
            if current_marbles < self.first_bet_prev_marbles:
                self.computer_declare = True
            else:
                self.computer_declare = False
            self.i_know_computer_declare = True
        return True
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        self.initialize_params()   # 추가!
        pos = self.current_position
        self.current_position += 1
        return self.glass_answer[pos]
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        # there are 4 types of persons
        # type1 corresponds a ordinary person who has standard stats for the game
        # type2 corresponds a person with great height
        # type3 corresponds a person with a lot of weight
        # type4 corresponds a person with strong power
        # the return should be a tuple with size of 4, and the sum of the elements should be 10
        # only for computer, it is allowed to set 12 members
        return (0, 3, 3, 4)


    def act_tugging_strategy(self, playground_tug_of_war):
        if playground_tug_of_war.player_condition['Computer'] == False:
            if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                print("case1")
                return 15
            else:
                print("case2")
                return 10
        else:
            if playground_tug_of_war.player_expression['Computer'] in ['best', 'well']:
                print("case3")
                return 30
            else:
                if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                    print("case4")
                    return 40 + random.randint(0, 10)
                else:
                    print("case5")
                    return random.randint(0, 2)
    # ================================================================================= for tug_of_war game