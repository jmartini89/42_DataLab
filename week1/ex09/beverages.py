class HotBeverage:
    def __init__(self, price = "0.30", name = "hot beverage") -> None:
        self.price = price
        self.name = name
    def description(self, desc = "Just some hot water in a cup") -> str:
        self.desc = desc
        return desc
    def __str__(self) -> str:
        return (
            "name : " + self.name + "\n" +
            "price : " + self.price + "\n"
            "description : " + self.description())

class Coffee(HotBeverage):
    def __init__(self) -> None:
        super().__init__("0.40", "coffee")
    def description(self) -> str:
        return super().description("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__("0.30", "tea")
    def description(self) -> str:
        return super().description()

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        super().__init__("0.50", "chocolate")
    def description(self) -> str:
        return super().description("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        super().__init__("0.45", "cappuccino")
    def description(self) -> str:
        return super().description("Un po' di Italia nella sua tazza!")

if __name__ == "__main__":

    BeverageCup = HotBeverage()
    CoffeeCup = Coffee()
    TeaCup = Tea()
    ChocolateCup = Chocolate()
    CappuccinoCup = Cappuccino()

    print(BeverageCup)
    print(CoffeeCup)
    print(TeaCup)
    print(ChocolateCup)
    print(CappuccinoCup)