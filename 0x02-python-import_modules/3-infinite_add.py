#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    result = 0
    for i in range(1, ln):
        result = result + int(sys.argv[i])
    print("{:d}".format(result))
