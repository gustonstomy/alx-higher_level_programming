#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = ()
    first_tup = tuple_a + (0, 0)
    second_tup = tuple_b + (0, 0)
    new_tup = second_tup[0] + first_tup[0], second_tup[1] + first_tup[1]
    return new_tup
