import os
import sys

__all__ = ('main',)
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def main():
    with open(os.path.join(__location__, "parrot.txt")) as f:
        for s in f:
            print(s.rstrip())

    for i, arg in enumerate(sys.argv):
        print("Arg:", i, "\tvalue:", arg)


if __name__ == '__main__':  
    main()

