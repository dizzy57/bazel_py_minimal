import sys


def main() -> None:
    print("Hello world!")
    print(sys.executable)
    print(sys.modules["__main__"].__file__)


if __name__ == "__main__":
    main()
