#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        n = fct(*args)
        return n
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
