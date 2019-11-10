from random import randint as rand
from basehandler import BaseHandler
from response import responseCodes


class GameHandle(BaseHandler):

    def __init__(self):
        super().__init__()
        self.random_number = None
        self.guess = None
        self.response = ""

    def run(self):
        self.random_number = rand(1, 10)
        self.input_guess()
        self.verify_guess()
        self.check_guess()
        self.play_again()

    def input_guess(self):
        self.guess = self.take_guess()

        if not self.guess:
            print("You must enter a valid guess.")
            self.run()

    def verify_guess(self):

        if not self.guess_verified(self.guess):
            print(self.guess_not_verified())
            self.input_guess()

    def check_guess(self):

        result = {}
        if self.random_number > 5:
            self.high_random_number(self.guess)
            self.response = self.high_random_number(self.guess)

        if self.random_number < 5:
            self.low_random_number(self.guess)
            self.response = self.low_random_number(self.guess)

        if self.response == responseCodes.CORRECT:
            self.money_addition()

        if self.response == responseCodes.WRONG:
            self.money_deduction()

        result["response_code"] = self.response
        result["message"] = f"Your current money is {self.get_current_money()}"
        result["random_number"] = self.random_number

        print(f"You are {result['response_code']}, {result['message']}\n")
        print(result)

    def play_again(self):

        if self.play(self.get_play_again_option()):
            self.run()

        self.exit()


if __name__ == "__main__":
    game = GameHandle()
    game.run()
