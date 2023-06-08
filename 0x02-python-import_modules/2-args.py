#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    if ln == 2:
        print("{:d} argument:".format(ln - 1))
    elif ln == 1:
        print("{:d} arguments.".format(ln - 1))
    else:
        print("{:d} arguments:".format(ln - 1))
    for i in range(1, ln):
        print("{:d}: {}".format(i, sys.argv[i]))
