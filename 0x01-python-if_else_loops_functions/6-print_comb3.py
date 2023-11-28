#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        first_digit = 0
        second_digit = i
    else :
        first_digit = i // 10
        second_digit = i % 10
    if first_digit < second_digit and int(f"{second_digit}{first_digit}") > i:
        print(f"{i:02}", end=", " if i != 89 else "\n")
