#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    div = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            pa
        div.append(result)
    return div
