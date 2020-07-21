class CoffeeMachine:
    VALID_COMMAND = ('buy', 'fill', 'take', 'remaining', 'exit')

    ESPRESSO = 1
    LATTE = 2
    CAPPUCCINO = 3

    COFFEE_TYPE = 3

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups_left = 9
        self.money = 550

    @staticmethod
    def getInt(prompt: str, /) -> int:
        """ get one integer in a line with prompt """
        print()
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
            except ValueError:
                pass
            else:
                return user_input

    def checkIngredients(self,
        water: int = 0,
        milk: int = 0,
        coffee_beans: int = 0
    ) -> bool:
        if self.water >= water \
            and self.milk >= milk \
            and self.coffee_beans >= coffee_beans \
            and self.cups_left > 0 \
        :
            return True

        print('\nSorry,', end=' ')
        if self.water < water:
            print('not enough water!', end=' ')
        if self.milk < milk:
            print('not enough milk!', end=' ')
        if self.coffee_beans < coffee_beans:
            print('not enough coffee beans!', end=' ')
        if self.cups_left == 0:
            print('not enough disposable cups!', end=' ')
        print()
        return False

    def updateIngredients(self,
        water: int = 0,
        milk: int = 0,
        coffee_beans: int = 0,
        money: int = 0
    ) -> None:
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.cups_left -= 1
        self.money += money

    def buyCoffee(self) -> None:
        print()
        while True:
            coffee_type = input(
                'What do you want to buy? '
                '1 - espresso, 2 - latte, '
                '3 - cappuccino, back - to main menu: ')
            if coffee_type == 'back':
                return

            try:
                coffee_type = int(coffee_type)
            except ValueError:
                continue

            if coffee_type in range(1, CoffeeMachine.COFFEE_TYPE + 1):
                break

        if coffee_type == CoffeeMachine.ESPRESSO:
            if self.checkIngredients(water=250, coffee_beans=16):
                self.updateIngredients(water=250, coffee_beans=16, money=4)
                print('\nI have enough resources, making you a coffee!')
        elif coffee_type == CoffeeMachine.LATTE:
            if self.checkIngredients(350, 75, 20):
                self.updateIngredients(350, 75, 20, 7)
                print('\nI have enough resources, making you a coffee!')
        elif coffee_type == CoffeeMachine.CAPPUCCINO:
            if self.checkIngredients(200, 100, 12):
                self.updateIngredients(200, 100, 12, 6)
                print('\nI have enough resources, making you a coffee!')

    def fillIngredients(self) -> None:
        water = CoffeeMachine.getInt(
            'Write how many ml of water do you want to add: ')
        milk = CoffeeMachine.getInt(
            'Write how many ml of milk do you want to add: ')
        coffee_beans = CoffeeMachine.getInt(
            'Write how many grams of coffee beans do you want to add : ')
        cups = CoffeeMachine.getInt(
            'Write how many disposable cups of coffee do you want to add: ')

        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups_left += cups

    def takeMoney(self) -> None:
        print(f'\nI gave you ${self.money}')
        self.money = 0

    def printSupplies(self) -> None:
        print('\nThe coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee_beans, 'of coffee beans')
        print(self.cups_left, 'of disposable cups')
        print(f'${self.money} of money')

    def activate(self) -> None:
        while True:
            print()
            while True:
                user_input = input(
                    f'Write action {CoffeeMachine.VALID_COMMAND}: ')
                if user_input in CoffeeMachine.VALID_COMMAND:
                    break

            if user_input == 'buy':
                self.buyCoffee()
            elif user_input == 'fill':
                self.fillIngredients()
            elif user_input == 'take':
                self.takeMoney()
            elif user_input == 'remaining':
                self.printSupplies()
            else:
                return


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.activate()


if __name__ == '__main__':
    main()
