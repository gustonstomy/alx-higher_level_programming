#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    listh = dir(hidden_4)
    listh.sort()
    for i in listh:
        if not(i.startswith("__")):
            print(i)
