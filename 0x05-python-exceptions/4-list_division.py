#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide each element of two lists by each other"""
    result_list = []
    for a in range(0, list_length):
        try:
            ans = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("Wrong type")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        except ZeroDivisionError:
            print("division by zero")
            ans = 0
        finally:
            result_list.append(ans)
    return (result_list)
