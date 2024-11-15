def demo1():
    print("I am module 2")

text = "module2"


class Person:
    pass


def main():
    print(__name__)
    print(text)
    demo1()


if __name__ == "__main__":
    main()