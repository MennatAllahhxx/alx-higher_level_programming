#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print("{}".format(i), end="")
            if i != 8 or j != 9:
                print("{}".format(j), end=", ")
            else:
                print("{}".format(j))
