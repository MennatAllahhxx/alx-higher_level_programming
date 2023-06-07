#!/usr/bin/python3
flag = 0
for i in range(ord('z'), ord('a') - 1, -1):
    if flag == 0:
        print("{:c}".format(i), end="")
        flag = 1
    else:
        j = chr(i - 32)
        print(j, end="")
        flag = 0
