#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lenght = len(sys.argv)
    sum = 0
    for i in range(1, lenght):
        sum += int(sys.argv[i])
    print(sum)
