import sys

__all__ = ('main',)


def main():
    for i, arg in enumerate(sys.argv):
        print("Arg:", i, "\tvalue:", arg)


if __name__ == '__main__':  
    main()
