from os import EX_OK


def my_var(arg):
    print(arg, type(arg))

my_var(42)
my_var("42")
my_var("quarante-deux")
my_var(42.0)
my_var(True)
my_var([42])
my_var({42: 42})
my_var((42,))
my_var(set())