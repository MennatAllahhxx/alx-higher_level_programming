#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    n = 0
    for i in range(list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            n = 0
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            newlist.append(n)
    return newlist
