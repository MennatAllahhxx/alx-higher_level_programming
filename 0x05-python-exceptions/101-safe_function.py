#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        n = fct(8args)
        return n
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
