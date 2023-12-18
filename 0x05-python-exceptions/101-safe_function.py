#!/usr/bin/python3
def safe_function(fct, *args):
    import sy
    try:
        tmp = fct(*args)
        return tmp
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
