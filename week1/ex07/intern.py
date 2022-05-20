class Intern:

    def __init__(self, name = "My name? I'm nobody, an intern, I have no name.") -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self) -> None:
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self) -> Coffee:
        return self.Coffee()

Nameless = Intern()
Mark = Intern("Mark")

print(Nameless)
print(Mark)

Coffee = Mark.make_coffee()
print(Coffee)

try:
    Nameless.work()
except Exception as e:
    print(str(e))