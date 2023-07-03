from Menu import MENU


class Inventory:
    def __init__(self):
        self.Menu = MENU
        self.Inv = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

    def CheckIfResourcesSufficient(self, CoffeeName: str) -> bool or list:
        NotEnough = [keys for keys in self.Menu[CoffeeName]['ingredients']
                     if not self.Inv[keys] >= self.Menu[CoffeeName]['ingredients'][keys]]
        return True if not NotEnough else NotEnough

    def DeductResources(self, CoffeeName: str):
        self.Inv.update({key: self.Inv[key] - self.Menu[CoffeeName]['ingredients'][key]
                         for key in self.Menu[CoffeeName]['ingredients'].keys()})

    def GetReport(self):
        print(f"*\tWater: {self.Inv['water']}ml",
              f"*\tMilk: {self.Inv['milk']}ml",
              f"*\tCoffee: {self.Inv['coffee']}g",
              f"*\tMoney: ${self.Inv['money']}",
              sep='\n')


class MakeCoffee(Inventory):
    def __init__(self):
        super().__init__()
        self.Pennies = {'nickles': 0.05, 'quarters': 0.25, 'pennies': 0.01, 'dimes': 0.10}

    def ProcessCoins(self, **kwargs):
        return self.Pennies['nickles'] * kwargs['nickels'] + self.Pennies['quarters'] * kwargs['quarters'] + \
            self.Pennies['pennies'] * kwargs['pennies'] + self.Pennies['dimes'] * kwargs['dimes']

    def CheckIfTransactionIsValid(self, CalculateTotal, prompt) -> float or bool:
        return False if CalculateTotal < self.Menu[prompt]['cost'] \
            else round(CalculateTotal - self.Menu[prompt]['cost'], 2)

    def Main(self):
        IsOn = True
        while IsOn:
            prompt = input('What would you like?(latte/espresso/cappuccino)\n'
                           'Type off to turn it OFF').lower()
            print()
            try:
                if prompt == 'report':
                    self.GetReport()
                elif prompt == 'off':
                    IsOn = False
                elif self.CheckIfResourcesSufficient(prompt) is True:
                    print('Please insert coins.')
                    CalculateTotal = self.ProcessCoins(nickels=int(input('how many nickels?: ')),
                                                       quarters=int(input('how many quarters?: ')),
                                                       pennies=int(input('how many pennies?: ')),
                                                       dimes=int(input('how many dimes?: ')))
                    GetStatus = self.CheckIfTransactionIsValid(CalculateTotal, prompt)
                    if isinstance(GetStatus, float):
                        if GetStatus > 0:
                            print(f'Here is ${GetStatus} dollars in change.')
                            self.DeductResources(prompt)
                            self.Inv['money'] += CalculateTotal - GetStatus
                            print(f'Here your {prompt} ☕️. Enjoy!')
                    else:
                        print("Sorry that's not enough money")
                else:
                    print(f'Sorry we ran out of {str(self.CheckIfResourcesSufficient(prompt))[1:-1]}')
            except KeyError:
                print('Please only enter advised prompts')


MakeCoffee = MakeCoffee()
MakeCoffee.Main()
