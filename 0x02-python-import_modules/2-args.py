#!/usr/bin/python3

if __name__ == "__main__":
    """Print the size of agrv and list its components."""
    import sys

    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size))
    for i in range(size):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
