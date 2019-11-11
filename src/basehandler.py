from src.response import responseCodes


class BaseHandler(object):

    def __init__(self):
        self.currennt_money = responseCodes.START_MONEY



    def take_guess(self):
        guess = int(input(responseCodes.OPTIONS))

        return guess



    def guess_verified(self, guess):
        options = [1, 2]

        if guess not in options:
            return False

        return True



    def guess_not_verified(self):
        return responseCodes.INVALID



    def high_random_number(self, guess):
        if guess == 1:
            return responseCodes.WRONG

        return responseCodes.CORRECT



    def low_random_number(self, guess):
        if guess == 1:
            return responseCodes.CORRECT

        return responseCodes.WRONG



    def money_addition(self):
        self.currennt_money += 10
        return self.currennt_money



    def money_deduction(self):
        self.currennt_money -= 10

        return self.currennt_money



    def get_current_money(self):
        return str(self.currennt_money)



    def get_play_again_option(self):
        option = int(input(responseCodes.PLAY_OPTIONS))

        return option



    def play(self, option):
        if option == 1:
            return True

        return False



    def exit(self):
        print(f"Thank you for playing. You've finished with {self.get_current_money()}")
        input()
        exit()



    def raise_guess_error(self):
        pass
