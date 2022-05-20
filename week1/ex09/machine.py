import random
import beverages

class EmptyCup(beverages.HotBeverage):
    def __init__(self, price="0.90", name="empty cup") -> None:
        super().__init__(price, name)
    def description(self, desc="An empty cup?! Gimme my money back!") -> str:
        return super().description(desc)

class BrokenMachine:
    def __init__(self) -> None:
        self.uses = 10
    class BrokenMachineException(Exception):
        def __init__(self, message = "This coffee machine has to be repaired.") -> None:
            self.message = message
            super().__init__(self.message)
    def repair(self) -> None:
        self.uses = 10
        print("Repairing...")
    def serve(self, Beverage: beverages.HotBeverage):
        if not self.uses:
            raise self.BrokenMachineException()
        self.uses -= 1
        if random.random() < 0.25:
            return EmptyCup()
        else:
            return Beverage

if __name__ == "__main__":

    Machine = BrokenMachine()

    options = [
        beverages.HotBeverage(),
        beverages.Coffee(),
        beverages.Tea(),
        beverages.Chocolate(),
        beverages.Cappuccino(),
    ]

    service = 0
    for x in range(25):
        try:
            service += 1
            print("#" + str(service))
            Cup = Machine.serve(options[random.randrange(0, len(options) - 1)])
            print(Cup)
        except Exception as e:
            print("- - -")
            service = 0
            print(e)
            Machine.repair()
            print("- - -")